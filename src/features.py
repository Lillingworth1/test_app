"""
Feature engineering for Titanic survival prediction.
"""
import pandas as pd
import numpy as np


def create_family_size(df):
    """
    Create a family size feature from SibSp and Parch.

    Args:
        df: DataFrame with SibSp and Parch columns

    Returns:
        pandas.DataFrame: DataFrame with FamilySize column added
    """
    df = df.copy()
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    return df


def create_is_alone(df):
    """
    Create a binary feature indicating if passenger is alone.

    Args:
        df: DataFrame with FamilySize column

    Returns:
        pandas.DataFrame: DataFrame with IsAlone column added
    """
    df = df.copy()
    if 'FamilySize' not in df.columns:
        df = create_family_size(df)
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    return df


def create_title_feature(df):
    """
    Extract title from Name column and create title feature.

    Args:
        df: DataFrame with Name column

    Returns:
        pandas.DataFrame: DataFrame with Title column added
    """
    df = df.copy()

    if 'Name' not in df.columns:
        return df

    # Extract title from name
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

    # Group rare titles
    title_mapping = {
        'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4,
        'Rev': 4, 'Col': 4, 'Major': 4, 'Mlle': 1, 'Countess': 2,
        'Ms': 1, 'Lady': 2, 'Jonkheer': 4, 'Don': 4, 'Dona': 2,
        'Mme': 2, 'Capt': 4, 'Sir': 4
    }

    df['Title'] = df['Title'].map(title_mapping)
    df['Title'].fillna(0, inplace=True)

    return df


def create_fare_bins(df):
    """
    Create fare bins for categorical representation.

    Args:
        df: DataFrame with Fare column

    Returns:
        pandas.DataFrame: DataFrame with FareBin column added
    """
    df = df.copy()

    if 'Fare' not in df.columns:
        return df

    # Create fare bins using quartiles
    df['FareBin'] = pd.qcut(df['Fare'], 4, labels=False, duplicates='drop')

    return df


def create_age_bins(df):
    """
    Create age bins for categorical representation.

    Args:
        df: DataFrame with Age column

    Returns:
        pandas.DataFrame: DataFrame with AgeBin column added
    """
    df = df.copy()

    if 'Age' not in df.columns:
        return df

    # Create age bins: Child (0-12), Teen (13-20), Adult (21-40), Middle (41-60), Senior (61+)
    df['AgeBin'] = pd.cut(df['Age'], bins=[0, 12, 20, 40, 60, 100],
                          labels=[0, 1, 2, 3, 4])

    return df


def engineer_all_features(df):
    """
    Apply all feature engineering steps.

    Args:
        df: Raw or preprocessed DataFrame

    Returns:
        pandas.DataFrame: DataFrame with all engineered features
    """
    df = create_family_size(df)
    df = create_is_alone(df)
    df = create_title_feature(df)
    df = create_fare_bins(df)
    df = create_age_bins(df)

    return df


if __name__ == '__main__':
    # Example usage
    from data_loader import load_data, preprocess_data

    print("Loading and preprocessing data...")
    df = load_data()
    df = preprocess_data(df)

    print("\nEngineering features...")
    df_features = engineer_all_features(df)

    print(f"Original columns: {len(df.columns)}")
    print(f"After feature engineering: {len(df_features.columns)}")
    print(f"\nNew features: {set(df_features.columns) - set(df.columns)}")
