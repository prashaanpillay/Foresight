from engine.src.structure.command.Command import Command
from ...services.PreprocessingService import PreprocessingService


class MapServicesCommand(Command):

    def execute(self):
        service = PreprocessingService(self.injector)
        self.injector.set_instance(PreprocessingService, service)
