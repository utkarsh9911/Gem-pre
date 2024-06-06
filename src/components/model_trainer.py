import pandas
import numpy

from src.logging.logger import logging
from src.exception.exception import customexception
import os 
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object,load_object,evaluate_model
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,RandomForest,xgboost

@dataclass


class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            raise customexception(e,sys)
        
      

