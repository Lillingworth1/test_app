"""
Machine learning model implementations for Titanic survival prediction.
"""
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

from data_loader import load_data, preprocess_data, split_features_target
from features import engineer_all_features


def prepare_data(test_size=0.2, random_state=42):
    """
    Load, preprocess, and split data for modeling.

    Args:
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # Load and preprocess data
    df = load_data()
    df = preprocess_data(df)
    df = engineer_all_features(df)

    # Split features and target
    feature_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
                       'Embarked', 'FamilySize', 'IsAlone', 'Title',
                       'FareBin', 'AgeBin']

    # Select only numeric columns that exist
    available_features = [col for col in feature_columns if col in df.columns]
    X = df[available_features]
    y = df['Survived']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    return X_train, X_test, y_train, y_test


def train_logistic_regression(X_train, y_train, max_iter=1000):
    """
    Train a Logistic Regression model.

    Args:
        X_train: Training features
        y_train: Training target
        max_iter: Maximum iterations for convergence

    Returns:
        LogisticRegression: Trained model
    """
    print("\nTraining Logistic Regression...")
    model = LogisticRegression(max_iter=max_iter, random_state=42)
    model.fit(X_train, y_train)
    print("Logistic Regression training complete")
    return model


def train_random_forest(X_train, y_train, n_estimators=100):
    """
    Train a Random Forest model.

    Args:
        X_train: Training features
        y_train: Training target
        n_estimators: Number of trees in the forest

    Returns:
        RandomForestClassifier: Trained model
    """
    print("\nTraining Random Forest...")
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=42,
        max_depth=10,
        min_samples_split=5
    )
    model.fit(X_train, y_train)
    print("Random Forest training complete")
    return model


def train_xgboost(X_train, y_train, n_estimators=100):
    """
    Train an XGBoost model.

    Args:
        X_train: Training features
        y_train: Training target
        n_estimators: Number of boosting rounds

    Returns:
        XGBClassifier: Trained model
    """
    print("\nTraining XGBoost...")
    model = XGBClassifier(
        n_estimators=n_estimators,
        random_state=42,
        max_depth=5,
        learning_rate=0.1,
        eval_metric='logloss'
    )
    model.fit(X_train, y_train)
    print("XGBoost training complete")
    return model


def save_model(model, model_name, output_dir='models'):
    """
    Save a trained model to disk.

    Args:
        model: Trained model object
        model_name: Name for the saved model file
        output_dir: Directory to save models

    Returns:
        Path: Path to saved model file
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Save model
    model_file = output_path / f"{model_name}.pkl"
    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_file}")
    return model_file


def load_model(model_path):
    """
    Load a trained model from disk.

    Args:
        model_path: Path to the saved model file

    Returns:
        object: Loaded model
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model


def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a trained model on test data.

    Args:
        model: Trained model
        X_test: Test features
        y_test: Test target
        model_name: Name of the model for display

    Returns:
        float: Accuracy score
    """
    print(f"\n{'='*50}")
    print(f"Evaluating {model_name}")
    print(f"{'='*50}")

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Print classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Died', 'Survived']))

    return accuracy


def train_all_models():
    """
    Train all models and save them to disk.

    Returns:
        dict: Dictionary containing all trained models
    """
    print("Preparing data...")
    try:
        X_train, X_test, y_train, y_test = prepare_data()
        print(f"Training set size: {len(X_train)}")
        print(f"Test set size: {len(X_test)}")
        print(f"Number of features: {X_train.shape[1]}")
    except FileNotFoundError:
        print("\nError: Titanic dataset not found!")
        print("Please download titanic.csv and place it in the data/ directory")
        return None

    # Train models
    models = {}

    # Logistic Regression
    lr_model = train_logistic_regression(X_train, y_train)
    models['logistic_regression'] = lr_model
    save_model(lr_model, 'logistic_regression')
    evaluate_model(lr_model, X_test, y_test, 'Logistic Regression')

    # Random Forest
    rf_model = train_random_forest(X_train, y_train)
    models['random_forest'] = rf_model
    save_model(rf_model, 'random_forest')
    evaluate_model(rf_model, X_test, y_test, 'Random Forest')

    # XGBoost
    xgb_model = train_xgboost(X_train, y_train)
    models['xgboost'] = xgb_model
    save_model(xgb_model, 'xgboost')
    evaluate_model(xgb_model, X_test, y_test, 'XGBoost')

    print("\n" + "="*50)
    print("All models trained and saved successfully!")
    print("="*50)

    return models


if __name__ == '__main__':
    # Train all models
    models = train_all_models()
