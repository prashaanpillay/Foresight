from engine.src.structure.service.Service import Service
from engine.src.structure.injector.Injector import Injector
from engine.src.model.DatasetModel import DatasetModel
from engine.src.utility.logger.Logger import Logger


class GrayscaleService(Service):

    def __init__(self, injector=Injector()):
        super().__init__(injector=injector)
        self.logger = self.injector.get_instance(Logger)
        self.dataset_model = self.injector.get_instance(DatasetModel)

    def convert(self):
        pass
