## Auckland Air Pollution Prediction
## Project Overview

This project focuses on predicting air pollution levels, specifically PM10 concentrations, in Auckland (NZ). Using historical air quality, weather, and traffic data, we employed advanced data science and machine learning (ML) techniques to model and forecast pollution patterns.

## Key Achievements

1. **Data Collection and Preparation**:
   - Collected and combined data from multiple sources, including air quality monitoring stations, weather records, and traffic flow statistics.
   - Addressed challenges (i.e., missing values and outliers) through robust data cleaning techniques.
   - Performed feature engineering by adding temporal (hour, day, season) and interaction features (e.g., wind speed × temperature).

2. **Exploratory Data Analysis (EDA)**:
   - Uncovered trends in PM10 levels, such as diurnal cycles (e.g., rush hour peaks) and seasonal variations (e.g., higher concentrations in winter).
   - Used correlation analysis to identify the most significant predictors, including temperature, wind speed, and traffic density.

3. **Model Development**:
   - Built and trained multiple ML models for PM10 prediction:
     - **Regression Models**: Linear Regression and Random Forests for interpretable results.
     - **Neural Networks**: Developed a Multilayer Perceptron (MLP) and Long Short-Term Memory (LSTM) network for time-series forecasting.
   - Compared model performance using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).

4. **Model Evaluation and Insights**:
   - Achieved accurate predictions with Random Forest and LSTM models outperforming simpler regression methods.
   - Provided insights into feature importance, demonstrating that wind speed, time of day, and traffic flow were the most impactful variables.

5. **Real-World Applications**:
   - Developed actionable predictions for urban planners and policymakers to mitigate air pollution during high-risk periods.
   - Demonstrated the potential for integration into real-time air quality monitoring systems.

### Key Challenges Addressed

- **Data Quality**: Handled missing values and inconsistent measurements across datasets.
- **Computational Complexity**: Optimised hyperparameters and batch processing for efficient neural network training.
- **Feature Interaction**: Accounted for complex relationships between weather, traffic, and PM10 levels using advanced feature engineering.

### Next Steps

- **Expand to Real-Time Analysis**: Integrate IoT sensors to provide dynamic and real-time pollution predictions.
- **Incorporate More Pollutants**: Extend the analysis to include other pollutants like PM2.5 and NO2 for a comprehensive air quality forecast.
- **Deploy as a Web App**: Build an interactive dashboard for live predictions and visualisations.

### Project Structure

- **`scripts/`**: Python scripts for data processing, model training, and evaluation.

- **`requirements.txt`**: List of dependencies required to run the project.

- **`README.md`**: Overview and instructions for the project.

- **`.gitignore`**: Specifies files and directories to be ignored by Git.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/auckland-pollution.git
   ```

2. **Navigate to the Project Directory**:
```bash
cd auckland-pollution
```

3. **Create a Virtual Environment**:
``bash

python -m venv venv
```
4. **Activate the Virtual Environment**:
On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash

source venv/bin/activate
```
5. **Install Dependencies**:
```bash

pip install -r requirements.txt
```
6. **Usage**
 - Data Pre-processing:
Run the data pre-processing script:
```bash

python scripts/data_preprocessing.py
```
 - Train Regression Models:
Execute the training script:
```bash

python scripts/train_regression_models.py
```
 - Train Neural Network Models:
Execute the training script:
```bash
python scripts/train_neural_networks.py
```
 - Evaluate Models:
Run the evaluation script:
```bash

python scripts/evaluate_models.py
```

### Contributing
Contributions are welcome. Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

