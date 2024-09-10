from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_trainning import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

def main():
   
    # data_ingestion = DataIngestionTrainingPipeline()
    # data_ingestion.execute()
    
    # prepare_base_model = PrepareBaseModelTrainingPipeline()
    # prepare_base_model.excute()
    
    # model_training = ModelTrainingPipeline()
    # model_training.excute()
    
    evaluation = EvaluationPipeline()
    evaluation.excute()

    
    
    
if __name__ == '__main__':
    main()