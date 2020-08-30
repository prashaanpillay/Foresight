from engine.src.structure.command.Command import Command
from engine.src.utility.logger.Logger import Logger
from engine.src.controller.command.StartupCommand import StartupCommand
from .preprocessing.PreprocessingCommand import PreprocessingCommand
from .acquisition.AcquisitionCommand import AcquisitionCommand


class OnStartupCommand(Command):

    def execute(self):
        self.command_map.execute(StartupCommand)

        logger = self.injector.get_instance(Logger)
        logger.progress("Foresight Started", heading=True)

        self.command_map.execute(AcquisitionCommand)

        # self.command_map.execute(PreprocessingCommand)

        logger.progress("Foresight Complete", heading=True)
