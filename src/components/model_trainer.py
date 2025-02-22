import os,sys
import yaml
import zipfile
import shutil
from src.utils.utils import read_yaml_file
from src.logger import logging
from src.exception import SignException
from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise SignException(e, sys)
    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")
        
        try:
            logging.info("Unzipping data")
            with zipfile.ZipFile("Sign_language_data.zip", 'r') as zip_ref:
                zip_ref.extractall() 
            os.remove("Sign_language_data.zip")
            
            if not os.path.exists("data.yaml"):
                raise FileNotFoundError("data.yaml not found after unzipping")
            
            # Get the number of classes from data.yaml
            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
                
            # Get the model config file name
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)
            
            # Update the number of classes in the model config file
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            config['nc'] = int(num_classes)
            
            # Write the updated config to a new file
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)
                
            #train
            os.system(f"cd yolov5/ && python train.py --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            
            # Copy the best model to artifacts directory
            best_model_path = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            if os.path.exists(best_model_path):
                shutil.copy(best_model_path, "yolov5/")
                os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
                shutil.copy(best_model_path, self.model_trainer_config.model_trainer_dir)
            else:
                raise FileNotFoundError(f"{best_model_path} not found")
           
            # Clean up
            shutil.rmtree("yolov5/runs", ignore_errors=True)
            shutil.rmtree("train", ignore_errors=True)
            shutil.rmtree("test", ignore_errors=True)
            os.remove("data.yaml")
            
            model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path="yolov5/best.pt",)

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact
            
        except Exception as e:
            raise SignException(e, sys)