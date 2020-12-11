from engine.src.structure.command.Command import Command
from engine.src.utility.logger.Logger import Logger
from engine.src.controller.command.StartupCommand import StartupCommand
from .preprocessing.PreprocessingCommand import PreprocessingCommand
from .acquisition.AcquisitionCommand import AcquisitionCommand
from .training.TrainingCommand import TrainingCommand


class OnStartupCommand(Command):

    def execute(self):
        self.command_map.execute(StartupCommand)

        logger = self.injector.get_instance(Logger)
        logger.progress("Foresight Started", heading=True)

        # TODO:find a way to skip commands but still having the config hydrated into the models at this point

        self.command_map.execute(AcquisitionCommand)
        self.command_map.execute(PreprocessingCommand)
        self.command_map.execute(TrainingCommand)

        logger.progress("Foresight Complete", heading=True)
