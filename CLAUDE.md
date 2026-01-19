# Titanic Survival Prediction - Claude Code Guide

## Project Overview

This is a machine learning project that predicts passenger survival on the Titanic. It's designed as a demo to showcase Claude Code's GitHub integration capabilities, including issue creation, tracking, and automated commits.

**Purpose**: Demonstrate AI-assisted development workflow with GitHub integration

## Commands

### Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Run data preprocessing
python src/data_loader.py

# Run feature engineering
python src/features.py

# Train and evaluate models
python src/models.py

# Run evaluation
python src/evaluate.py
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_data_loader.py
```

### Data Download
```bash
# The Titanic dataset can be downloaded from Kaggle
# Place titanic.csv in the data/ directory
```

## Project Architecture

### Directory Structure
```
test_app/
├── data/                   # Dataset files
│   └── titanic.csv        # Main dataset
├── src/                   # Source code
│   ├── data_loader.py     # Data loading and preprocessing
│   ├── features.py        # Feature engineering functions
│   ├── models.py          # ML model implementations
│   └── evaluate.py        # Model evaluation and metrics
├── notebooks/             # Jupyter notebooks for exploration
├── tests/                 # Unit tests
│   ├── test_data_loader.py
│   ├── test_features.py
│   └── test_models.py
├── requirements.txt       # Python dependencies
├── CLAUDE.md             # This file - AI assistant guide
└── README.md             # Project documentation
```

### Module Descriptions

**data_loader.py**
- `load_data()`: Loads Titanic CSV dataset
- `preprocess_data()`: Handles missing values, converts categorical variables
- `split_features_target()`: Separates features from target variable

**features.py**
- `create_family_size()`: Creates FamilySize feature from SibSp + Parch
- `create_is_alone()`: Binary feature for solo passengers
- `create_title_feature()`: Extracts and maps titles from passenger names
- `create_fare_bins()`: Bins fare into quartiles
- `create_age_bins()`: Bins age into categories
- `engineer_all_features()`: Applies all feature engineering

**models.py**
- Implements Logistic Regression, Random Forest, and XGBoost
- Trains models on preprocessed data
- Saves trained models to disk
- Generates predictions

**evaluate.py**
- Calculates accuracy, precision, recall, F1-score
- Generates confusion matrices
- Compares model performance
- Creates visualization plots

## GitHub Workflow

### Commit Convention
All commits **MUST** reference an issue number using the format:
```
<action> <description> #<issue-number>
```

Examples:
- `Add data preprocessing functions #1`
- `Implement Random Forest model #2`
- `Fix missing value handling #5`
- `Update README with setup instructions #3`

### Issue Labels

**Type Labels:**
- `feature` - New functionality
- `bug` - Something isn't working
- `enhancement` - Improvement to existing feature
- `documentation` - Documentation updates
- `testing` - Test coverage improvements

**Priority Labels:**
- `P0-critical` - Must be done immediately
- `P1-high` - Important, should be next
- `P2-medium` - Normal priority
- `P3-low` - Nice to have

**Component Labels:**
- `data` - Data loading, preprocessing
- `models` - ML model implementations
- `features` - Feature engineering
- `evaluation` - Model evaluation and metrics
- `infrastructure` - Setup, dependencies, tooling

### Working with Issues

When starting work on an issue:
1. Comment on the issue: "Starting work on [issue description]"
2. Create commits that reference the issue number
3. Comment with progress updates if the task is complex
4. Close the issue with a summary comment when complete

### Creating Issues

Issues should include:
- Clear, descriptive title
- Detailed description of what needs to be done
- Appropriate labels (type, priority, component)
- Acceptance criteria when relevant

## Development Practices

### Code Style
- Follow PEP 8 for Python code
- Use descriptive variable names
- Add docstrings to all functions
- Keep functions focused and single-purpose

### Testing
- Write unit tests for all new functions
- Aim for >80% code coverage
- Test edge cases and error conditions
- Use pytest fixtures for common setup

### Documentation
- Update README.md when adding features
- Keep CLAUDE.md synchronized with project changes
- Add inline comments for complex logic
- Document function parameters and return values

## Common Tasks

### Adding a New Feature
1. Create an issue describing the feature
2. Label appropriately (feature, priority, component)
3. Implement the feature following project conventions
4. Add unit tests
5. Update documentation
6. Make commits referencing the issue
7. Close the issue with summary

### Fixing a Bug
1. Create or work on existing bug issue
2. Reproduce the bug with a test case
3. Implement the fix
4. Verify the test passes
5. Commit with issue reference
6. Close the issue

### Improving Documentation
1. Create documentation issue
2. Update relevant files (README.md, CLAUDE.md, docstrings)
3. Commit with issue reference
4. Close the issue

## Dataset Information

The Titanic dataset includes:
- **PassengerId**: Unique identifier
- **Survived**: Target variable (0 = No, 1 = Yes)
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **Name**: Passenger name
- **Sex**: Male or female
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Fare**: Passenger fare
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## Key Features to Demonstrate

This project showcases:
1. **GitHub issue creation** - Claude creates well-structured issues
2. **Issue tracking** - Comments on issues as work progresses
3. **Commit conventions** - All commits reference issue numbers
4. **Task completion** - Issues are closed with summaries
5. **Label management** - Appropriate labels applied automatically
6. **Code quality** - Following best practices and conventions
