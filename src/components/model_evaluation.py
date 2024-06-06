import os
import sys
from sklearn.metrics import mean_squared_error,mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import save_object,load_object,evaluate_model
from dataclasses import dataclass
from src.logging.logger import logging
from src.exception.exception import customexception


@dataclass


class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise customexception(e,sys)
        
      

