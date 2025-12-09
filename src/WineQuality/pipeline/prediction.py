import joblib 
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        # End-to-End-Wine-Quality-Prediction\artifacts\model_trainer\model.joblib
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction