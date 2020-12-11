from engine.src.structure.command.Command import Command
from ..models.TrainingModel import TrainingModel


class MapModelCommand(Command):

    def execute(self):
        self.injector.as_singleton(TrainingModel)
