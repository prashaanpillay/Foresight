from engine.src.structure.command.Command import Command
from ..models.TrainingConfigModel import TrainingConfigModel


class MapModelCommand(Command):

    def execute(self):
        self.injector.as_singleton(TrainingConfigModel)
