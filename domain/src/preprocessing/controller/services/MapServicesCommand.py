from engine.src.structure.command.Command import Command
from ...services.GrayscaleService import GrayscaleService


class MapServicesCommand(Command):

    def execute(self):
        service = GrayscaleService(self.injector)
        self.injector.set_instance(GrayscaleService, service)
