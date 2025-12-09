from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQuality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from WineQuality.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from WineQuality.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
     
   
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_Validation = DataValidationTrainingPipeline()
   data_Validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
     
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_Transformation = DataTransformationTrainingPipeline()
   data_Transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
     
STAGE_NAME = "Model Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelTrainingPipeline()
   model_training.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
   
STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_eval = ModelEvaluationPipeline()
   model_eval.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e