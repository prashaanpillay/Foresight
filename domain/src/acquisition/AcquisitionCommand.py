from engine.src.structure.command.Command import Command
from .controller.RetrieveDatasetCommand import RetrieveDatasetCommand

class AcquisitionCommand(Command):

    def execute(self):
        retrieveDatasetCommand = RetrieveDatasetCommand()
        self.command_map.execute(retrieveDatasetCommand)