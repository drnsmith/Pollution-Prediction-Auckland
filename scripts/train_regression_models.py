import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load cleaned data
data = pd.read_csv('data/processed/cleaned_data.csv')

# Feature engineering
X = data[['Temperature', 'WindSpeed', 'Traffic']]
y = data['PM10']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Save model
import pickle
with open('models/regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)
