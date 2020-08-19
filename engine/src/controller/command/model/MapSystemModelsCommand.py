from ....structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel


class MapSystemModelsCommand(Command):

    def execute(self):
        datasetModel_model = self.injector.as_singleton(DatasetModel)
