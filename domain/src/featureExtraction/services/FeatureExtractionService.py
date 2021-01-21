from engine.src.structure.service.Service import Service
from engine.src.structure.injector.Injector import Injector
from engine.src.model.DatasetModel import DatasetModel
from engine.src.utility.logger.Logger import Logger
import importlib


class FeatureExtractionService(Service):

    def __init__(self, injector=Injector()):
        super().__init__(injector=injector)
        self.logger = self.injector.get_instance(Logger)
        self.dataset_model = self.injector.get_instance(DatasetModel)
        self.feature_extraction_command = None

    def addFeatureExtractionCommand(self, command_name):
        self.logger.progress("Adding " + str(command_name) + " to feature extraction pipeline")
        self.feature_extraction_command = (self.__resolve_class(command_name))

    def extract(self):
        training_dataset = self.dataset_model.training_dataset
        for candidate_model in training_dataset:
            self.feature_extraction_command.execute(candidate_model)

    @staticmethod
    def __resolve_class(class_name):
        split_on_class_name = str(class_name).split('.')[-1]
        string_class_name = split_on_class_name.split('\'')[0]

        module = importlib.import_module(class_name.__module__)
        class_ = getattr(module, string_class_name)
        instance = class_()
        return instance
