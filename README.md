# 💓 Heart Disease Prediction App

This project is a complete machine learning pipeline for predicting heart disease using clinical data.  
It includes preprocessing, feature selection, modeling, and a deployed web interface using Streamlit.

---

```
                
  
  
## 🗂️ Project Structure


Heart_Disease_Project/
│── data/
│ └── heart_disease.csv
│── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_pca_analysis.ipynb
│ ├── 03_feature_selection.ipynb
│ ├── 04_supervised_learning.ipynb
│ ├── 05_unsupervised_learning.ipynb
│ └── 06_hyperparameter_tuning.ipynb
│── models/
│ └── final_model.pkl
│── ui/
│ └── app.py # Streamlit Web Interface
│── deployment/
│ └── ngrok_setup.txt # Instructions to run app online via Ngrok
│── results/
│ └── evaluation_metrics.txt
│── used_features.json # Final selected features for prediction
│── requirements.txt # Python dependencies
│── .gitignore
│── README.md

``` 

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Heart_Disease_Project.git
cd Heart_Disease_Project


2. Install dependencies:

pip install -r requirements.txt


🚀 Run the Streamlit App Locally

cd ui
streamlit run app.py


🌐 Deploy using Ngrok (Free)
Sign up on Ngrok and copy your authtoken.

Authenticate Ngrok:

ngrok config add-authtoken YOUR_AUTHTOKEN

3. Run your Streamlit app:

streamlit run app.py


4. In another terminal, expose port 8501:

ngrok http 8501


5. Use the public link provided by Ngrok (e.g. https://abc123.ngrok-free.app).


🧠 Models Used

Logistic Regression

Random Forest

Decision Tree

PCA + Clustering (Unsupervised)


🛠 Requirements
See: requirements.txt



📬 Contact
For any questions, feel free to reach out to [amotaz792@gmail.com ].

نسخ
ت
