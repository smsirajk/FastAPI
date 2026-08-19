**⚡ FastAPI + Streamlit ML App**

**📌 Introduction** 

This repository contains an end‑to‑end machine learning application built with FastAPI and Streamlit. The backend trains and serves a RandomForest Classifier using the insurance.csv dataset, while the frontend provides an interactive UI for predictions.

**🧠 Machine Learning Pipeline Dataset: **

insurance.csv (user demographics, lifestyle, and income data).

Model: RandomForest Classifier (scikit‑learn).

Features engineered: BMI, lifestyle risk, age group, city tier.

Output: Model saved as model.pkl and exposed via FastAPI.

Predictions include:

Predicted insurance premium category.

Confidence score.

Probability distribution across all classes.

⚙️ Tech Stack FastAPI → REST API backend

Streamlit → Frontend web app

Scikit‑learn → ML model training

Pandas / NumPy → Data preprocessing

Pickle → Model persistence

📂 Repository Structure Code . ├── app.py # FastAPI backend ├── frontend.py # Streamlit frontend ├── model/ # Trained model (model.pkl) ├── schema/ # Pydantic schemas ├── config/ # Configurations ├── insurance.csv # Training dataset ├── requirements.txt # Dependencies └── README.md # Documentation 🚀 Getting Started

Clone the repository bash git clone https://github.com/your-username/fastapi-streamlit-insurance.git cd fastapi-streamlit-insurance

Install dependencies bash pip install -r requirements.txt

Run FastAPI backend bash uvicorn app:app --reload --port 8000 API docs available at: 👉 http://127.0.0.1:8000/docs

Run Streamlit frontend bash streamlit run frontend.py Frontend available at: 👉 http://localhost:8501

**🔗 Example API Usage POST /predict**

json { "age": 30, "weight": 70, "height": 1.75, "income_lpa": 15, "smoker": "no", "city": "Kolkata", "occupation": "Data Scientist" } Response

json { "predicted_category": "Premium_Tier_2", "confidence": 0.87, "class_probabilities": { "Premium_Tier_1": 0.05, "Premium_Tier_2": 0.87, "Premium_Tier_3": 0.08 } }

**🎯 Features**

End‑to‑end ML workflow (train → save → serve → predict).

FastAPI backend with auto‑generated Swagger docs.

Streamlit frontend for interactive predictions.

Modular structure for scalability and future enhancements.

**📌 Roadmap** 

Add Docker support for deployment.

Integrate MLflow for model versioning.

Deploy to cloud (AWS/Azure/GCP).

Add probability visualization in Streamlit.
