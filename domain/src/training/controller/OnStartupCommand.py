from engine.src.structure.command.Command import Command
from .MapModelCommand import MapModelCommand
from .PopulateConfigModelCommand import PopulateConfigModelCommand


class OnStartupCommand(Command):

    def execute(self):
        self.command_map.execute(MapModelCommand)
        self.command_map.execute(PopulateConfigModelCommand)
