from engine.src.structure.command.Command import Command
from .controller.services.MapServicesCommand import MapServicesCommand
from .services.FeatureExtractionService import FeatureExtractionService
from .controller.operations.featureExtractionCommands.SiftFeatureMatchCommand import SiftFeatureMatchCommand


class FeatureExtractionCommand(Command):

    def execute(self):
        self.command_map.execute(MapServicesCommand)

        service = self.injector.get_instance(FeatureExtractionService)
        service.addFeatureExtractionCommand(SiftFeatureMatchCommand)
        service.extract()
