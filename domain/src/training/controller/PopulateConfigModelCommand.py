from engine.src.structure.command.Command import Command
from ..models.TrainingConfigModel import TrainingConfigModel
from engine.src.utility.parsers.JsonParser import JsonParser
from engine.src.utility.assetLoader.AssetLoader import AssetLoader


class PopulateConfigModelCommand(Command):

    def execute(self):
        assetLoader = self.injector.get_instance(AssetLoader)
        training_config = JsonParser.decode(
            assetLoader.get_config('training.json'))
        trainingConfigModel = self.injector.get_instance(TrainingConfigModel)
        trainingConfigModel.set_data(training_config)
