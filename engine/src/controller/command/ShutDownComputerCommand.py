from ...structure.command.Command import Command
import os


class ShutDownComputerCommand(Command):

    def execute(self):

        os.system("shutdown /s /t 1")
