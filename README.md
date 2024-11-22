## Auckland Air Pollution Prediction

### Overview

This project aims to predict air pollution levels in Auckland using regression and neural network models. The goal is to provide accurate forecasts to aid in environmental planning and public health awareness.

### Project Structure
```python
auckland-pollution/ ├── data/ │ ├── raw/ │ ├── processed/ ├── notebooks/ ├── scripts/ ├── models/ ├── reports/ ├── requirements.txt ├── README.md └── .gitignore
```

- **`data/`**: Contains datasets.
  - `raw/`: Original datasets.
  - `processed/`: Cleaned and transformed datasets.

- **`notebooks/`**: Jupyter notebooks for data pre-processing, analysis, and modelling.

- **`scripts/`**: Python scripts for data processing, model training, and evaluation.

- **`models/`**: Serialised models saved after training.

- **`reports/`**: Documentation and reports related to the project.

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
