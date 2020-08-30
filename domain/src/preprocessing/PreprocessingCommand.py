from engine.src.structure.command.Command import Command
from .controller.services.MapServicesCommand import MapServicesCommand
from .controller.operations.GrayScaleCommand import GrayscaleCommand
from .services.PreprocessingService import PreprocessingService
from .controller.operations.GrayScaleCommand import GrayscaleCommand
from .controller.operations.AveragingBlurCommand import AveragingBlurCommand

class PreprocessingCommand(Command):

    def execute(self):
        self.command_map.execute(MapServicesCommand)
        
        service = self.injector.get_instance(PreprocessingService)        
        service.addPreprocessingCommand(AveragingBlurCommand)
        service.addPreprocessingCommand(GrayscaleCommand)
        service.convert()
