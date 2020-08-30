from ..injector.Injector import Injector


class Model:

    def __init__(self, injector=Injector()):
        self.injector = injector

    def update(self, config):
        pass

    def dispose(self):
        pass
