from engine.src.structure.command.Command import Command
from .controller.services.MapServicesCommand import MapServicesCommand
from .controller.operations.spatialCommands.BlurCommand import BlurCommand
from .services.PreprocessingService import PreprocessingService


class PreprocessingCommand(Command):

    def execute(self):
        self.command_map.execute(MapServicesCommand)

        service = self.injector.get_instance(PreprocessingService)
        service.addPreprocessingCommand(BlurCommand)
        # service.addPreprocessingCommand(GrayscaleCommand)
        # service.convert()
