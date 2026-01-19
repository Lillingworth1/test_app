# Titanic Survival Prediction

A machine learning project that predicts passenger survival on the Titanic using various classification models.

## Features

- Data preprocessing and exploratory analysis
- Multiple ML models (Logistic Regression, Random Forest, XGBoost)
- Feature engineering (family size, titles, fare bins)
- Model evaluation and comparison
- Predictions export to CSV

## Project Structure

```
test_app/
├── data/               # Dataset files
├── src/               # Source code
│   ├── data_loader.py    # Data loading and preprocessing
│   ├── features.py       # Feature engineering
│   ├── models.py         # ML model implementations
│   └── evaluate.py       # Model evaluation
├── notebooks/         # Jupyter notebooks for exploration
├── tests/            # Unit tests
├── requirements.txt  # Dependencies
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the model:
```bash
python src/models.py
```

## Testing

```bash
pytest tests/
```

## Data

Uses the classic Titanic dataset with passenger information including:
- Age, Sex, Passenger Class
- Fare, Embarkation Port
- Number of siblings/spouses and parents/children aboard

## Models

- **Logistic Regression**: Baseline model
- **Random Forest**: Ensemble method
- **XGBoost**: Gradient boosting

## License

MIT
