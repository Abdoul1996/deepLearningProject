import sys
from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging


class TrainPipeline:
    def __init__(self):
        """
        Initializes the TrainPipeline class with the data ingestion configuration.
        """
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process.

        Returns:
            DataIngestionArtifact: Contains details about the ingested data.
        
        Raises:
            XRayException: If an error occurs during the data ingestion process.
        """
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from the S3 bucket")

            # Initialize the DataIngestion process
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )
            
            # Run the data ingestion process
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Successfully retrieved train_set and test_set from S3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            
            return data_ingestion_artifact
        except Exception as e:
            logging.error(f"Error in start_data_ingestion: {str(e)}")
            raise XRayException(e, sys)


if __name__ == "__main__":
    # Initialize the TrainPipeline and run data ingestion
    train_pipeline = TrainPipeline()
    try:
        data_ingestion_artifact = train_pipeline.start_data_ingestion()
        logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
    except Exception as e:
        logging.error(f"Pipeline execution failed: {str(e)}")
