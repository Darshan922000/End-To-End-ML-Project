# It will have some common thing which we probabli going to use in our project...

import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj, file)

    except Exception as e:
        raise CustomException(e, sys)
    
def evalute_models(X_train, y_train, X_test, y_test, models):
        try:
            report = {}

            for i in range(len(list(models))):
                model = list(models.values())[i]
                model.fit(X_train, y_train)
                train_pred = model.predict(X_train)
                test_pred = model.predict(X_test)

                train_accuracy = r2_score(y_train, train_pred)
                test_accuracy = r2_score(y_test, test_pred)

                report[list(models.keys())[i]] = test_accuracy

            return report
        
        except Exception as e:
            raise CustomException(e, sys)
        