import pandas as pd
from hate.constants import EXPECTED_IMBALANCED_COLUMNS, EXPECTED_RAW_COLUMNS
from hate.exception import CustomException
from hate.entity.artifact_entity import DataValidationArtifact
import sys

class DataValidation:
    def __init__(self, data_ingestion_artifact):
        self.data_ingestion_artifact = data_ingestion_artifact

    def validate_dataset(self, file_path, expected_columns):
        try:
            # Read the dataset
            df = pd.read_csv(file_path)

            # Check if the dataset has the expected columns
            actual_columns = list(df.columns)
            if sorted(actual_columns) != sorted(expected_columns):
                return False, f"Column names do not match for file {file_path}. Expected: {expected_columns}, but got: {actual_columns}"

            # Check if the dataset has the expected number of columns
            if len(actual_columns) != len(expected_columns):
                return False, f"Column count mismatch for file {file_path}. Expected: {len(expected_columns)}, but got: {len(actual_columns)}"

            return True, None

        except Exception as e:
            raise CustomException(e,sys)

    def validate(self):
        try:
            # Initialize DataValidationArtifact
            validation_artifact = DataValidationArtifact()

            # Validate the imbalance dataset
            imbalance_valid, imbalance_error = self.validate_dataset(
                self.data_ingestion_artifact.imbalance_data_file_path,
                EXPECTED_IMBALANCED_COLUMNS
            )
            validation_artifact.imbalance_dataset_valid = imbalance_valid
            validation_artifact.imbalance_dataset_error = imbalance_error

            # Validate the raw dataset
            raw_valid, raw_error = self.validate_dataset(
                self.data_ingestion_artifact.raw_data_file_path,
                EXPECTED_RAW_COLUMNS
            )
            validation_artifact.raw_dataset_valid = raw_valid
            validation_artifact.raw_dataset_error = raw_error

            return validation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e
