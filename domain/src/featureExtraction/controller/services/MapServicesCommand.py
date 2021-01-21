from engine.src.structure.command.Command import Command
from ...services.FeatureExtractionService import FeatureExtractionService


class MapServicesCommand(Command):

    def execute(self):
        service = FeatureExtractionService(self.injector)
        self.injector.set_instance(FeatureExtractionService, service)
