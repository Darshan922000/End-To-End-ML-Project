
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def pred(self, features):
        try:
            model_path = "./data storage/model.pkl"
            preprocessor_path = "./data storage/preprocessor.pkl"

            logging.info("Model and preprocessor is loading...!!")
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            logging.info("Model and preprocessor has loaded...!!")
            logging.info(f"type of preprocessor is {type(preprocessor)} & type of model is {type(model)}")
            logging.info(f"features are {features}")
            scaled_data = preprocessor.transform(features)
            logging.info(f"preprocessing is done...Scaled data is {scaled_data}, {type(scaled_data)}, {scaled_data.shape}!!")
            prediction = model.predict(scaled_data)
            return prediction
        
        except Exception as e:
            raise CustomException(e, sys)


    


