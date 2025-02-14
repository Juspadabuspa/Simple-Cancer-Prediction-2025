import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle


def create_model(data):
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']
    
    # Scale data, keep numbers close
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Split the data
    X_Train, X_Test, Y_Train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the data
    model = LogisticRegression()
    model.fit(X_Train, Y_Train)
    
    # Test model 
    
    Y_pred = model.predict(X_Test)
    accuracy = accuracy_score(Y_test, Y_pred)
    class_report = classification_report(Y_test, Y_pred)
    print(f"Accuracy of our model: {accuracy}")
    print(f"Classification Report: {class_report}")
    
    return model, scaler # Scaler is used for predictions
    

def get_clean_data():
    data = pd.read_csv("Data/data.csv")
    
    # Drop unnecessary columns
    data.drop(["Unnamed: 32", "id"], axis=1, inplace=True)
    
    # Convert diagnosis column to binary
    data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
    
    # Drop rows with missing values
    data.dropna(inplace=True)
    
    return data



    


def main():
    data = get_clean_data()
    
    model, scaler = create_model(data)
    
    with open('model/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('model/scaler.pkl', 'wb') as g:
        pickle.dump(scaler, g)
    
    
    
if __name__ == '__main__':
    main()

