from engine.src.structure.command.Command import Command
from .imageTraining.loadImages.LoadTrainingImagesCommand import LoadTrainingImagesCommand
from .imageTraining.loadImages.LoadValidationImagesCommand import LoadValidationImagesCommand
from .StartFittingComand import StartFittingCommand
from .controller.OnStartupCommand import OnStartupCommand


class TrainingCommand(Command):

    def execute(self):
        self.command_map.execute(OnStartupCommand)
        self.command_map.execute(LoadTrainingImagesCommand)
        self.command_map.execute(LoadValidationImagesCommand)
        self.command_map.execute(StartFittingCommand)
