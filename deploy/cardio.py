import pandas as pd

class Cardio():
  
    def data_preparation(self, df):                    # cleaning, preparation, feature engineering and enconding
        
        # Age in years
        df['age_years'] = df['age'] / 360

        # Drop the columns 'id' and 'age' and target 'cardio'
        df.drop(['id','age', 'cardio'], axis='columns', inplace=True)

        # Creating feature 'IMC'
        df1 = df.copy()
        df1['IMC'] = df1['weight']/((df1['height']/100) * (df1['height']/100))

        # Creating feature 'dwarfism'
        df1['dwarfism'] = [1 if value < 145 else 0 for value in df1['height']]

        # Creating feature 'blood_pressure' manually as a dummie
        df1['blood_pressure_1'] = df1[['ap_hi', 'ap_lo']].apply(lambda x: 1 if (x['ap_hi'] < 90) & (x['ap_lo'] < 60) else 0, axis=1)
        df1['blood_pressure_2'] = df1[['ap_hi', 'ap_lo']].apply(lambda x: 1 if (90 <= x['ap_hi'] < 140) & (60 <= x['ap_lo'] < 90) else 0, axis=1)
        df1['blood_pressure_3'] = df1[['ap_hi', 'ap_lo']].apply(lambda x: 1 if (140 <= x['ap_hi'] < 160) & (90 <= x['ap_lo'] < 100) else 0, axis=1)
        df1['blood_pressure_4'] = df1[['ap_hi', 'ap_lo']].apply(lambda x: 1 if (x['ap_hi'] >= 160) & (x['ap_lo'] >= 100) else 0, axis=1)
        df1['blood_pressure_5'] = df1[['ap_hi', 'ap_lo']].apply(lambda x: 0 if (x['ap_hi'] < 90) & (x['ap_lo'] < 60) else
                                                                0 if (90 <= x['ap_hi'] < 140) & (60 <= x['ap_lo'] < 90) else
                                                                0 if (140 <= x['ap_hi'] < 160) & (90 <= x['ap_lo'] < 100) else
                                                                0 if (x['ap_hi'] >= 160) & (x['ap_lo'] >= 100) else
                                                                1, axis=1)

        # Create cholesterol dummie variable manually
        df1['cholesterol_1'] = df1[['cholesterol']].apply(lambda x: 1 if x['cholesterol'] == 1 else 0, axis=1)
        df1['cholesterol_2'] = df1[['cholesterol']].apply(lambda x: 1 if x['cholesterol'] == 2 else 0, axis=1)
        df1['cholesterol_3'] = df1[['cholesterol']].apply(lambda x: 1 if x['cholesterol'] == 3 else 0, axis=1)

        # Create gluc dummie variable manually
        df1['gluc_1'] = df1[['gluc']].apply(lambda x: 1 if x['gluc'] == 1 else 0, axis=1)
        df1['gluc_2'] = df1[['gluc']].apply(lambda x: 1 if x['gluc'] == 2 else 0, axis=1)
        df1['gluc_3'] = df1[['gluc']].apply(lambda x: 1 if x['gluc'] == 3 else 0, axis=1)

        # Drop the columns
        df1.drop(['cholesterol', 'gluc'], axis='columns', inplace=True)

        return df1
    
    def get_prediction(self, model, original_data, test_data):
        
        # Prediction
        pred = model.predict(test_data)
        
        # Join prediction into the original data
        original_data['prediction'] = pred
        
        return original_data.to_json(orient='records')