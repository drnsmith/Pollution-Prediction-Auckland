### AI-Powered Air Quality Prediction with Regression Models and Advanced Machine Learning Techniques (LSTM)

#### **Overview**
This project focuses on predicting air pollution levels, specifically **PM10** concentrations, in Auckland, New Zealand. By utilising historical data on air quality, weather conditions, and traffic patterns, the project employs advanced data science and machine learning techniques to model and forecast pollution trends.

---

#### **Key Achievements**
- **Data Collection and Preparation**:
  - Aggregated data from multiple sources, including air quality monitoring stations, meteorological records, and traffic flow statistics.
  - Addressed challenges such as missing values and outliers through robust data cleaning methods.
  - Engineered features by incorporating temporal elements (e.g., hour, day, season) and interaction terms (e.g., wind speed × temperature).

- **Exploratory Data Analysis (EDA)**:
  - Identified trends in PM10 levels, such as diurnal cycles (e.g., rush hour peaks) and seasonal variations (e.g., higher concentrations in winter).
  - Conducted correlation analysis to determine significant predictors, including temperature, wind speed, and traffic density.

- **Model Development**:
  - Developed and trained multiple machine learning models for PM10 prediction:
    - **Regression Models**: Linear Regression and Random Forests for interpretable results.
    - **Neural Networks**: Constructed a Multilayer Perceptron (MLP) and Long Short-Term Memory (LSTM) network for time-series forecasting.
  - Evaluated model performance using metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).

- **Model Evaluation and Insights**:
  - Achieved accurate predictions, with Random Forest and LSTM models outperforming simpler regression methods.
  - Provided insights into feature importance, highlighting that wind speed, time of day, and traffic flow were the most impactful variables.

- **Real-World Applications**:
  - Offered actionable predictions for urban planners and policymakers to mitigate air pollution during high-risk periods.
  - Demonstrated potential integration into real-time air quality monitoring systems.

---

## **Project Structure**
- **`scripts/`**: Contains Python scripts for data processing, model training, and evaluation.
- **`requirements.txt`**: Lists dependencies required to run the project.
- **`README.md`**: Provides an overview and instructions for the project.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/drnsmith/Pollution-Prediction-Auckland.git
cd Pollution-Prediction-Auckland
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
```

### **3. Activate the Virtual Environment**
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **1. Data Pre-processing**
Run the data pre-processing script to clean and prepare the data:
```bash
python scripts/data_preprocessing.py
```

### **2. Train Regression Models**
Execute the training script for regression models:
```bash
python scripts/train_regression_models.py
```

### **3. Train Neural Network Models**
Execute the training script for neural network models:
```bash
python scripts/train_neural_networks.py
```

### **4. Evaluate Models**
Run the evaluation script to assess model performance:
```bash
python scripts/evaluate_models.py
```

---

### Productisation  
This air quality prediction system can be developed into a **real-time environmental monitoring platform**, offering **live air pollution forecasts** for policymakers, city planners, and environmental agencies. By integrating with **IoT sensors and satellite data**, the system can provide **dynamic air quality predictions** across different regions. A potential **API service** could allow researchers and businesses to query pollution forecasts for specific locations, enabling **data-driven decision-making** in urban planning and public health initiatives.

### Monetisation  
The project can be monetised through a **subscription-based SaaS model**, offering **custom air quality predictions** to **government agencies, environmental research firms, and businesses**. A **freemium model** could provide **basic pollution forecasts**, while premium plans could include **detailed trend analysis, risk alerts, and industry-specific insights**. Additionally, licensing the **pollution forecasting API** to **smart city projects, transport authorities, and climate tech startups** presents another revenue stream.


---
### Contributing
This project was a collaborative effort between Natasha Smith and Elaheh Bastani. We would like to acknowledge each other’s contribution in designing, implementing, and executing the entire pipeline, from data collection and cleaning to sentiment analysis and visualisation. Our complementary skills made this project a success.
Contributions are welcome! If you have ideas or improvements to share, please follow these steps:

1. **Fork the Repository:**
Create your own copy of the repository by clicking the "Fork" button at the top right of this page.

2. **Create a Feature Branch:**
Work on your changes in a dedicated branch.

```bash
git checkout -b feature/YourFeatureName
```
3. **Commit Your Changes:**
Write clear and concise commit messages explaining what you’ve done.

```bash
git commit -m "Add YourFeatureName"
```
4. **Push Your Changes**:
Push your feature branch to your forked repository.
```bash
git push origin feature/YourFeatureName
```
5. **Open a Pull Request**:
Submit your changes to the main repository by opening a pull request (PR). Ensure your PR description explains your changes clearly.

6. **Review and Feedback**:
We will review your PR and may suggest improvements before merging it into the main branch.

Thank you for your interest in contributing!

---
## Repository History Cleaned

As part of preparing this repository for collaboration, its commit history has been cleaned. This action ensures a more streamlined project for contributors and removes outdated or redundant information in the history. 

The current state reflects the latest progress as of 24/01/2025.

For questions regarding prior work or additional details, please contact the author.

---

### License
Distributed under the MIT License. See `LICENSE` for more information.


