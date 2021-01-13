from engine.src.structure.command.Command import Command
from .controller.RetrieveDatasetCommand import RetrieveDatasetCommand
from .controller.FilterOutCorruptedImagesCommand import FilterOutCorruptedImagesCommand


class AcquisitionCommand(Command):

    def execute(self):
        self.command_map.execute(RetrieveDatasetCommand)
        self.command_map.execute(FilterOutCorruptedImagesCommand)
