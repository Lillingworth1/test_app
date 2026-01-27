"""
Data loading and preprocessing for Titanic survival prediction.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def load_data(file_path='data/titanic.csv'):
    """
    Load the Titanic dataset.

    Args:
        file_path: Path to the CSV file

    Returns:
        pandas.DataFrame: Loaded dataset
    """
    df = pd.read_csv(file_path)
    return df


def impute_missing_values(df, include_target=True):
    """
    Impute missing values using MICE (Multiple Imputation by Chained Equations).

    Uses scikit-learn's IterativeImputer which models each feature with missing values
    as a function of other features in a round-robin fashion.

    Args:
        df: DataFrame with potential missing values
        include_target: Whether to include Survived column in imputation model

    Returns:
        pandas.DataFrame: DataFrame with imputed values
    """
    df = df.copy()

    # Drop columns with too many missing values (Cabin) and non-numeric columns
    # Keep Name for title extraction later
    columns_to_drop = ['Cabin', 'Ticket', 'PassengerId']
    df_impute = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Convert categorical variables to numeric before imputation
    df_impute['Sex'] = df_impute['Sex'].map({'male': 0, 'female': 1})
    df_impute['Embarked'] = df_impute['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    # Store Name column separately (can't impute text)
    name_col = df_impute['Name'].copy() if 'Name' in df_impute.columns else None
    df_impute = df_impute.drop('Name', axis=1, errors='ignore')

    # Get columns with missing values
    missing_cols = df_impute.columns[df_impute.isnull().any()].tolist()

    if missing_cols:
        print(f"Imputing missing values in columns: {missing_cols}")
        print(f"Missing value counts before imputation:")
        for col in missing_cols:
            print(f"  {col}: {df_impute[col].isnull().sum()}")

        # Determine which columns to use for imputation
        if include_target and 'Survived' in df_impute.columns:
            impute_cols = df_impute.columns.tolist()
        else:
            impute_cols = [col for col in df_impute.columns if col != 'Survived']

        # Create imputer - uses Bayesian Ridge regression by default
        imputer = IterativeImputer(
            max_iter=10,
            random_state=42,
            verbose=0
        )

        # Fit and transform
        df_imputed = pd.DataFrame(
            imputer.fit_transform(df_impute[impute_cols]),
            columns=impute_cols,
            index=df_impute.index
        )

        # Copy back non-imputed columns if Survived was excluded
        if not include_target and 'Survived' in df_impute.columns:
            df_imputed['Survived'] = df_impute['Survived']

        # Add Name column back
        if name_col is not None:
            df_imputed['Name'] = name_col

        print(f"\nImputation complete. All missing values filled.")
    else:
        df_imputed = df_impute
        if name_col is not None:
            df_imputed['Name'] = name_col

    return df_imputed


def preprocess_data(df, use_mice_imputation=True):
    """
    Preprocess the Titanic dataset.

    Args:
        df: Raw dataframe
        use_mice_imputation: If True, use MICE imputation; if False, use simple median/mode

    Returns:
        pandas.DataFrame: Preprocessed dataframe
    """
    # Create a copy to avoid modifying original
    df = df.copy()

    if use_mice_imputation:
        # Use MICE (Multiple Imputation by Chained Equations)
        # This models missing values using other features including Survived
        df = impute_missing_values(df, include_target=True)
    else:
        # Simple imputation (legacy method)
        df['Age'] = df['Age'].fillna(df['Age'].median())
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())

        # Drop Cabin (too many missing values)
        df = df.drop('Cabin', axis=1, errors='ignore')

        # Convert Sex to numeric
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

        # Convert Embarked to numeric
        df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    return df


def split_features_target(df, target_column='Survived'):
    """
    Split dataframe into features and target.

    Args:
        df: Preprocessed dataframe
        target_column: Name of the target column

    Returns:
        tuple: (X, y) features and target
    """
    # Select numeric columns for features
    feature_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

    X = df[feature_columns]
    y = df[target_column]

    return X, y


if __name__ == '__main__':
    # Example usage
    print("Loading Titanic data...")
    df = load_data()
    print(f"Loaded {len(df)} rows")

    print("\nPreprocessing data with MICE imputation...")
    df_processed = preprocess_data(df, use_mice_imputation=True)
    print("Preprocessing complete")

    X, y = split_features_target(df_processed)
    print(f"\nFeatures shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"\nMissing values after preprocessing: {df_processed.isnull().sum().sum()}")
