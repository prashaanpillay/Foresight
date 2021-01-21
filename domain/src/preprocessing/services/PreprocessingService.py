from engine.src.structure.service.Service import Service
from engine.src.structure.injector.Injector import Injector
from engine.src.model.DatasetModel import DatasetModel
from engine.src.utility.logger.Logger import Logger
from pathlib import Path
import importlib


class PreprocessingService(Service):

    def __init__(self, injector=Injector()):
        super().__init__(injector=injector)
        self.logger = self.injector.get_instance(Logger)
        self.dataset_model = self.injector.get_instance(DatasetModel)
        self.preprocessing_command_queue = []

    def addPreprocessingCommand(self, command_name):
        self.logger.progress("Adding " + str(command_name) + " to preprocessing")
        self.preprocessing_command_queue.append(self.__resolve_class(command_name))

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def convert(self):
        threads = 1
        # TODO: Add in validadation set to be preprocessed
        paths = self.chunks((list(Path(self.dataset_model.training_directory).rglob('*.png')) + (list(Path(self.dataset_model.validation_directory).rglob('*.png)')))), threads)
        for path in paths:
            self.do_so_work(path)

    def do_so_work(self, paths):
        for path in paths:
            print(path)
            for command in self.preprocessing_command_queue:
                command.execute(imagePath=str(path))

    @staticmethod
    def __resolve_class(class_name):
        split_on_class_name = str(class_name).split('.')[-1]
        string_class_name = split_on_class_name.split('\'')[0]

        module = importlib.import_module(class_name.__module__)
        class_ = getattr(module, string_class_name)
        instance = class_()
        return instance
