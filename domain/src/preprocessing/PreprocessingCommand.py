from engine.src.structure.command.Command import Command
from .controller.services.MapServicesCommand import MapServicesCommand
from .controller.operations.GrayScaleCommand import GrayscaleCommand


class PreprocessingCommand(Command):

    def execute(self):
        mapServicesCommand = MapServicesCommand()
        self.command_map.execute(mapServicesCommand)

        gray_scale_command = GrayscaleCommand()
        self.command_map.execute(gray_scale_command)
