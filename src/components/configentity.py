import os
from dataclasses import dataclass



@dataclass   # use it only when we need to add only parameter...if want to add functions go with the full mode...!!!
class DataIngestionConfig:
    train_data_path: str = os.path.join("data storage", "train.csv")
    test_data_path: str = os.path.join("data storage", "test.csv")
    raw_data_path: str = os.path.join("data storage", "data.csv")