from engine.src.structure.command.Command import Command
from .controller.services.MapServicesCommand import MapServicesCommand
from .controller.operations.spatialCommands.GrayScaleCommand import GrayscaleCommand
from .services.PreprocessingService import PreprocessingService
from .controller.operations.spatialCommands.GrayScaleCommand import GrayscaleCommand

class PreprocessingCommand(Command):

    def execute(self):
        self.command_map.execute(MapServicesCommand)
        
        service = self.injector.get_instance(PreprocessingService)
        service.addPreprocessingCommand(GrayscaleCommand)
        service.convert()
