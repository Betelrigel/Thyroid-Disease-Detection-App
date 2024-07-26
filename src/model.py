from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df):
    X = df.drop('classes', axis=1)
    y = df['classes']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'model.pkl')
    
    return model, X_test, y_test
