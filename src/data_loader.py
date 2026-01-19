"""
Data loading and preprocessing for Titanic survival prediction.
"""
import pandas as pd
import numpy as np
from pathlib import Path


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


def preprocess_data(df):
    """
    Preprocess the Titanic dataset.

    Args:
        df: Raw dataframe

    Returns:
        pandas.DataFrame: Preprocessed dataframe
    """
    # Create a copy to avoid modifying original
    df = df.copy()

    # Fill missing Age values with median
    df['Age'].fillna(df['Age'].median(), inplace=True)

    # Fill missing Embarked with mode
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Fill missing Fare with median
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

    # Drop Cabin (too many missing values)
    df.drop('Cabin', axis=1, inplace=True, errors='ignore')

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

    print("\nPreprocessing data...")
    df_processed = preprocess_data(df)
    print("Preprocessing complete")

    X, y = split_features_target(df_processed)
    print(f"\nFeatures shape: {X.shape}")
    print(f"Target shape: {y.shape}")
