from ...structure.command.Command import Command
from .model.MapSystemModelsCommand import MapSystemModelsCommand
from engine.src.controller.command.OnSystemStartupCommand import OnSystemStartupCommand

class StartupCommand(Command):

    def execute(self):
        system_startup = OnSystemStartupCommand()
        self.command_map.execute(system_startup)

        map_models_command = MapSystemModelsCommand()
        self.command_map.execute(map_models_command)
