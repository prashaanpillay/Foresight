from ..injector.Injector import Injector


class Service:

    def __init__(self, injector=Injector()):
        self.injector = injector
        self.service_name = self.__class__.__name__