import pandas as pd
import pickle
import tensorflow as tf
from sklearn.metrics import mean_absolute_error

# Load cleaned data
data = pd.read_csv('data/processed/cleaned_data.csv')

# Feature engineering
X = data[['Temperature', 'WindSpeed', 'Traffic']]
y = data['PM10']

# Load models
with open('models/regression_model.pkl', 'rb') as file:
    regression_model = pickle.load(file)

neural_network_model = tf.keras.models.load_model('models/neural_network_model.h5')

# Evaluate models
regression_predictions = regression_model.predict(X)
nn_predictions = neural_network_model.predict(X)

print(f"Regression Model MAE: {mean_absolute_error(y, regression_predictions)}")
print(f"Neural Network MAE: {mean_absolute_error(y, nn_predictions)}")
