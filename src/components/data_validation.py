import os, sys
import shutil
from src.logger import logging
from src.exception import SignException
from src.entity.config_entity import DataValidationConfig
from src.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)
        
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            list_of_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            
            for file in list_of_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                    break

                else:
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.validation_status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            
            return validation_status
                
        except Exception as e:
            raise SignException(e, sys)
    
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            
            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                logging.info("Copy data successfully")
            
            return data_validation_artifact
        
        except Exception as e:
            raise SignException(e, sys)