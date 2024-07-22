import sys
from hate.components.data_ingestion import DataIngestion
from hate.components.data_validation import DataValidation
from hate.entity.artifact_entity import DataIngestionArtifact
from hate.entity.config_entity import DataIngestionConfig
from hate.exception import CustomException
from hate.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from S3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from S3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            
            logging.info("Exited the run_pipeline method of TrainPipeline class") 
             # Data Validation
            # Data Validation
            data_validation = DataValidation(data_ingestion_artifacts)
            validation_artifacts = data_validation.validate()

            # Print detailed validation results
            if validation_artifacts.imbalance_dataset_valid:
                print("Imbalance dataset validation passed.")
            else:
                print(f"Imbalance dataset validation failed: {validation_artifacts.imbalance_dataset_error}")

            if validation_artifacts.raw_dataset_valid:
                print("Raw dataset validation passed.")
            else:
                print(f"Raw dataset validation failed: {validation_artifacts.raw_dataset_error}")

        except Exception as e:
            raise CustomException(e, sys) from e
        
        
# if __name__=="__main__":
#     train_pipeline=TrainPipeline()
#     train_pipeline.start_data_ingestion()