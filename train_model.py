import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def clean_data(df):
    # Dropping the 'referral source' column
    df = df.drop('referral source', axis=1)
    
    # Mapping 'classes' to binary values
    df['classes'] = df['classes'].map({'negative.': 0, 'positive.': 1})
    
    # Converting categorical data
    df['sex'] = df['sex'].map({'M': 1, 'F': 0})
    
    # Filling NaN values with mean of respective columns
    df.fillna(df.mean(), inplace=True)
    
    return df

def train_model(df):
    X = df.drop('classes', axis=1)
    y = df['classes']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'model.pkl')
    print("Model saved to model.pkl")
    
    return model, X_test, y_test

# Load and preprocess the dataset
try:
    df = pd.read_csv('thyroid_data.csv')
    df = clean_data(df)
    print("Data loaded and cleaned successfully.")
except Exception as e:
    print(f"Error loading or cleaning data: {e}")

# Train the model and save it
try:
    model, X_test, y_test = train_model(df)
    print("Model trained and saved successfully.")
except Exception as e:
    print(f"Error training or saving model: {e}")

# Check if model.pkl exists
if os.path.exists('model.pkl'):
    print("model.pkl exists in the current directory.")
else:
    print("model.pkl does not exist.")
