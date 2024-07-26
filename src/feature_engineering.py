from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    scaler = StandardScaler()
    
    # Convert categorical variables to numeric (if needed)
    df['sex'] = df['sex'].map({'F': 0, 'M': 1})
    
    # Scale numeric features
    numeric_features = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
    df[numeric_features] = scaler.fit_transform(df[numeric_features])
    
    # Drop irrelevant columns (if any)
    df.drop(['referral source'], axis=1, inplace=True)
    
    # Convert classes to binary (if needed)
    df['classes'] = df['classes'].map({'negative.': 0, 'positive.': 1})
    
    return df
