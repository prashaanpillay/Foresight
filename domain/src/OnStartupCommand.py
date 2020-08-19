from engine.src.structure.command.Command import Command
from engine.src.utility.logger.Logger import Logger
from engine.src.controller.command.StartupCommand import StartupCommand
from .preprocessing.PreprocessingCommand import PreprocessingCommand
from .acquisition.AcquisitionCommand import AcquisitionCommand


class OnStartupCommand(Command):

    def execute(self):
        system_startup = StartupCommand()
        self.command_map.execute(system_startup)

        logger = self.injector.get_instance(Logger)
        logger.progress("Foresight Started", heading=True)

        acquisitionCommand = AcquisitionCommand()
        self.command_map.execute(acquisitionCommand)

        preprocessingCommand = PreprocessingCommand()
        self.command_map.execute(preprocessingCommand)

        logger.progress("Foresight Complete", heading=True)
