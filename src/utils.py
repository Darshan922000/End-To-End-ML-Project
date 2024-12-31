# It will have some common thing which we probabli going to use in our project...

import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file:
            dill.dump(obj, file)

    except Exception as e:
        raise CustomException(e, sys)