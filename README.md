# Heart Disease Prediction App 💓

This is a machine learning pipeline to detect heart disease using clinical parameters.  
It includes preprocessing, modeling, and a deployed Streamlit web UI.

## 💾 Files Included
- `preprocessing/`: Scripts for cleaning and encoding data.
- `models/`: Trained `.pkl` files.
- `notebooks/`: Full Jupyter Notebooks for each phase.
- `app.py`: Streamlit interface.
- `requirements.txt`: All required packages.
- `used_features.json`: Final selected features.

Heart_Disease_Project/
│── data/
│ ├── heart_disease.csv
│── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ ├── 06_hyperparameter_tuning.ipynb
│── models/
│ ├── final_model.pkl
│── ui/
│ ├── app.py (Streamlit UI)
│── deployment/
│ ├── ngrok_setup.txt
│── results/
│ ├── evaluation_metrics.txt
│── README.md
│── requirements.txt
│── .gitignore


## 🚀 Run the App

1. Install dependencies:
```bash
pip install -r requirements.txt
