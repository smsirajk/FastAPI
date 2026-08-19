 #!/usr/bin/env python
# coding: utf-8
# In[9]:
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model, MODEL_VERSION
from schema.prediction_response import PredictionResponse

#import the MI model

app = FastAPI()

# Human readable, welcome of the page
@app.get('/')
def home():
    return {'message':'Insuranced Premium Prediction API'}

# Machine, API readable page

@app.get('/health')
def health_check():
    return {
        'Status': 'OK',
        'version': MODEL_VERSION,
        'model_Loaded': model is not None

    }

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'Response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

