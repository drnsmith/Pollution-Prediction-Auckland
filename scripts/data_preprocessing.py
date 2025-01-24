import pandas as pd

# Load raw data
data = pd.read_csv('data/raw/original_dataset.csv')

# Preprocessing steps
data.fillna(method='ffill', inplace=True)  # Fill missing values
data.to_csv('data/processed/cleaned_data.csv', index=False)

print("Data preprocessing completed. Cleaned data saved to 'data/processed/cleaned_data.csv'.")
