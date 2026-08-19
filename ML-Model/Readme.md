📊 Insurance Premium Prediction – FastAPI + Streamlit
🌟 Project Overview
This project is an end‑to‑end Machine Learning application that predicts insurance premium categories based on user attributes.
It combines:

FastAPI → to serve the trained ML model as a REST API.

RandomForest Classifier → trained on insurance.csv dataset.

Streamlit → as the frontend interface for user interaction.

The goal is to demonstrate how to train, deploy, and consume a machine learning model seamlessly using modern Python frameworks.


🧠 Machine Learning Workflow
Dataset:

Source: insurance.csv

Contains features like age, weight, height, income, smoker status, city, and occupation.

Model Training:

Algorithm: RandomForest Classifier

Preprocessing: Feature engineering (BMI, lifestyle risk, city tier, age group).

Output: Model saved as model.pkl for reuse.

Prediction Output:

Predicted category (e.g., premium tier).

Confidence score.

Probability distribution across all classes.

⚙️ Tech Stack
Backend: FastAPI, Pydantic, Uvicorn

Frontend: Streamlit

ML: Scikit‑learn, Pandas, NumPy

Serialization: Pickle

📂 Project Structure
Code
.
├── app.py                  # FastAPI backend with ML endpoints
├── frontend.py             # Streamlit frontend application
├── model/                  # Trained model (model.pkl)
├── schema/                 # Pydantic schemas for validation
├── config/                 # Configurations
├── insurance.csv           # Training dataset
├── requirements.txt        # Dependencies
└── README.md               # Documentation
🚀 How to Run
1. Clone the repository
bash
git clone https://github.com/your-username/fastapi-insurance-app.git
cd fastapi-insurance-app
2. Install dependencies
bash
pip install -r requirements.txt
3. Start FastAPI server
bash
uvicorn app:app --reload --port 8000
API available at:
👉 http://127.0.0.1:8000/docs

4. Run Streamlit frontend
bash
streamlit run frontend.py
Frontend available at:
👉 http://localhost:8501

🔗 API Endpoints
POST /predict → Accepts JSON input and returns prediction with confidence and class probabilities.

Sample Request:

json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 15,
  "smoker": "no",
  "city": "Kolkata",
  "occupation": "Data Scientist"
}
Sample Response:

json
{
  "predicted_category": "Premium_Tier_2",
  "confidence": 0.87,
  "class_probabilities": {
    "Premium_Tier_1": 0.05,
    "Premium_Tier_2": 0.87,
    "Premium_Tier_3": 0.08
  }
}
🎯 Features
End‑to‑end ML pipeline (train → save → serve → predict).

FastAPI backend with auto‑generated Swagger docs.

Streamlit frontend for interactive predictions.

Modular project structure for scalability.

📌 Future Enhancements
Add Docker for containerized deployment.

Integrate MLflow for model versioning and tracking.

Enhance frontend with visual probability charts.

Deploy to cloud (Azure/AWS/GCP) for public access.
