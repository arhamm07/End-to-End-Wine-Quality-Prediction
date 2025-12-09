from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.save_results()
        