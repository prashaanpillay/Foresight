from ....structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from engine.src.model.DatasetImageGeneratorModel import DatasetImageGeneratorModel


class MapSystemModelsCommand(Command):

    def execute(self):
        self.injector.as_singleton_with_injector(DatasetModel)
        self.injector.as_singleton_with_injector(DatasetImageGeneratorModel)
