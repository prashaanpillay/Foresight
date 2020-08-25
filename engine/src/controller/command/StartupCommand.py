from ...structure.command.Command import Command
from .model.MapSystemModelsCommand import MapSystemModelsCommand
from engine.src.controller.command.OnSystemStartupCommand import OnSystemStartupCommand


class StartupCommand(Command):

    def execute(self):
        self.command_map.execute(OnSystemStartupCommand)
        self.command_map.execute(MapSystemModelsCommand)
