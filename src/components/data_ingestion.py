import os
import sys
from src.exception import CustomException # For handling the errors
from src.logger import logging            # For printing log messages
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
@dataclass 
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") # Path to save training data
    test_data_path: str=os.path.join('artifacts',"test.csv")   # Path to save testing data
    raw_data_path: str=os.path.join('artifacts',"data.csv")    # Path to save raw data

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # Creating config object with paths

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Step 1: Read the dataset from a CSV file
            df=pd.read_csv('notebook/Data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # Step 2: Create folder if it doesn’t exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # Step 3: Save raw data (original copy)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # Step 4: Split data into training and testing sets
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            # Step 5: Save both train and test datasets as CSV files
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            # Step 6: Return file paths for next steps
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            # If any error happens, raise it as a CustomException
            raise CustomException(e,sys)
        
if __name__=="__main__":
    # Step 1: Creating an object of DataIngestion class
    obj=DataIngestion()
    # Step 2: Running the ingestion method to get train and test data paths
    train_data,test_data=obj.initiate_data_ingestion()
    # Step 3: Creating an object of DataTransformation class
    data_transformation=DataTransformation()
    # Step 4: Running the transformation (cleaning and preparing the data)
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # Step 5: Creating an object of ModelTrainer class
    modeltrainer=ModelTrainer()
    # Step 6: Training the model and printing the score
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


