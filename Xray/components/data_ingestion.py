import sys 

from Xray.cloud_storage.s3_operation import S3Operation
from Xray.entity.artifact_entity import DataIngestionArtifact 
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException 
from Xray.logger import logging 


class DataIngestion:
    
    def __init__(self):
        pass
    
    # get the data from S3
    def get_data_from_s3(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)
        
        # initiate data ingestion 

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)
