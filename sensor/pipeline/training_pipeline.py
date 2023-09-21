from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from sensor.components.data_ingestion import DataIngestion
class TrainingPipeline:

    def __init__(self,training_pipleine_config:TrainingPipelineConfig):
        try:
            self.training_pipleine_config=training_pipleine_config
        except Exception as e:
            raise SensorException(e, sys)


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion_config =DataIngestionConfig(
                training_pipeline_config=self.training_pipleine_config)
            
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)
    def start(self,):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)