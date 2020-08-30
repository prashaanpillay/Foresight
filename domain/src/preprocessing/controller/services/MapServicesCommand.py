from engine.src.structure.command.Command import Command
from ...services.PreprocessingService import PreprocessingService


class MapServicesCommand(Command):

    def execute(self):
        self.injector.as_singleton_with_injector(PreprocessingService)
