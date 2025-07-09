# Heart Disease Prediction App 💓

A machine learning pipeline to predict heart disease using clinical data.  
Built using Python, Scikit-learn, and Streamlit.

## 💻 Files Included
- `App.py`: Streamlit UI
- `pipeline_model2.joblib`: Trained model pipeline
- `used_features2.json`: List of used features
- `heart_disease_cleaned.csv`: Dataset
- `requirements.txt`: Required libraries

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run ui/App.py

---

```
## 🗂️ Project Structure

Heart_Disease_Project/
│
├── data/
│   └── heart_disease_cleaned.csv
│
├── models/
│   └── pipeline_model2.joblib
│
├── ui/
│   └── App.py
│
├── used_features2.json
├── requirements.txt
├── README.md 


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
