import pickle, joblib
import pandas as pd
from flask import Flask, request, Response
from cardio import Cardio

# Load model
model = pickle.load(open('C:/Users/Usuario/Desktop/Data_Science/PROJETOS_DATA_SCIENCE/Projeto_Cardio_Disease/deploy/model_LGBM.pkl', 'rb'))

# Inicialize API
app = Flask(__name__)
@app.route('/cardio/predict', methods=['POST'])
def cardio_predict():
    test_json = request.get_json()
    
    if test_json:   #There is data
        if isinstance(test_json, dict):                        # unique example
            test_raw = pd.DataFrame(test_json, index=[0])  
        else:                                                  # multiple examples  
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Cardio Class
        pipeline = Cardio()
        
        # Data preparation
        df2 = pipeline.data_preparation(test_raw)
        
        # Prediction
        df_response = pipeline.get_prediction(model, test_raw, df2)
        
        return df_response
        
        
    else: 
        return Response('{}', status=200, mimetype='application/json')
        

if __name__ == '__main__':
    app.run('0.0.0.0')