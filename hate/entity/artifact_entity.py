from dataclasses import dataclass
from typing import Optional

@dataclass
class DataIngestionArtifact:
    # Data ingestion artifacts
    imbalance_data_file_path: str
    raw_data_file_path: str

@dataclass
class DataValidationArtifact:
    # Validation results for imbalance dataset
    imbalance_dataset_valid: Optional[bool] = None
    imbalance_dataset_error: Optional[str] = None
    
    # Validation results for raw dataset
    raw_dataset_valid: Optional[bool] = None
    raw_dataset_error: Optional[str] = None

@dataclass
class DataTransformationArtifact:
    transformed_data_path:str

@dataclass
class ModelTrainerArtifacts: 
    trained_model_path:str
    x_test_path: list
    y_test_path: list

@dataclass
class ModelEvaluationArtifacts:
    is_model_accepted: bool 

@dataclass
class ModelPusherArtifacts:
    bucket_name: str
