from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    # Data ingestion artifacts
    imbalance_data_file_path: str
    raw_data_file_path: str