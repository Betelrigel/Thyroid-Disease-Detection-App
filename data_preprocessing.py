import pandas as pd

def clean_data(df):
    # Replace '?' with NaN in entire dataframe
    df.replace('?', pd.NA, inplace=True)
    
    # Print unique values in each column to identify the problematic column
    for col in df.columns:
        unique_values = df[col].unique()
        print(f"Column '{col}' unique values: {unique_values}")
    
    # Handle specific columns with non-numeric values
    # Example: Convert 'sex' column from categorical to numeric
    df['sex'] = df['sex'].map({'F': 0, 'M': 1})  # Convert categorical to numeric
    
    # Handle missing values in numeric columns
    numeric_cols = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
    df[numeric_cols] = df[numeric_cols].astype(float)  # Convert numeric columns to float
    
    df.fillna(df.mean(), inplace=True)  # Replace NaN with mean in numeric columns
    
    return df
