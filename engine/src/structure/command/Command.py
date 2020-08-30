from .CommandMap import CommandMap
from ..injector.Injector import Injector


class Command:

    def __init__(self, injector=Injector()):
        self.injector = injector
        self.command_map = CommandMap()

        # TODO: Find a way to set logger up earlier in order to exxecute this
        print("Executing: "+str(type(self).__name__))

    def execute(self):
        pass

    def startup(self):
        pass

    def destroy(self):
        self.injector.destroy()
        self.command_map.destroy()
        self.injector = None
        self.command_map = None
