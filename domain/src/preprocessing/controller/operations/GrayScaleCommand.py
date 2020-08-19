from engine.src.structure.command.Command import Command
from ...services.GrayscaleService import GrayscaleService


class GrayscaleCommand(Command):

    def execute(self):
        gray_scale_service = self.injector.get_instance(GrayscaleService)
        gray_scale_service.convert()
