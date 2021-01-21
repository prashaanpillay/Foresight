from engine.src.structure.command.Command import Command
from engine.src.utility.assetLoader.AssetLoader import AssetLoader
from engine.src.utility.logger.Logger import Logger
from engine.src.utility.parsers.JsonParser import JsonParser
from engine.src.model.DatasetModel import DatasetModel
from ..models.CandidateModel import CandidateModel
import os
import pandas


class RetrieveDatasetCommand(Command):

    def __init__(self):
        super().__init__()
        self.logger = self.injector.get_instance(Logger)
        self.dataset_model = self.injector.get_instance(DatasetModel)
        self.assetLoader = self.injector.get_instance(AssetLoader)

        self.acquisition_config = JsonParser.decode(self.assetLoader.get_config('acquisition.json'))
        self.dataset = self.acquisition_config['dataset']
        self.raw_directory = os.path.abspath("assets/raw_set/")
        self.build = self.acquisition_config['build']

    def get_path(self, path):
        return os.path.abspath(self.raw_directory + "\\" + path)

    def read_in_pickle_files(self):
        candidate_training_models = []
        validation_training_models = []

        training_dataframe = pandas.read_pickle(self.raw_directory + self.dataset["training_set_input_directory"])

        for row in training_dataframe.iterrows():
            candidate_model = CandidateModel()
            candidate_model.update(row[1]['survey_id'], self.get_path(row[1]['anchor_image_path']), row[1]['transform'], self.get_path(row[1]['ref_image_path']), self.get_path(row[1]['target_image_path']))
            candidate_training_models.append(candidate_model)
            candidate_model.write_out_given(self.dataset_model.training_directory)
            break

        validation_dataframe = pandas.read_pickle(self.raw_directory + self.dataset["validation_set_input_directory"])

        for row in validation_dataframe.iterrows():
            candidate_model = CandidateModel()
            candidate_model.update(row[1]['survey_id'], self.get_path(row[1]['anchor_image_path']), row[1]['transform'], self.get_path(row[1]['ref_image_path']), self.get_path(row[1]['target_image_path']))
            validation_training_models.append(candidate_model)
            candidate_model.write_out_given(self.dataset_model.validation_directory)

        self.dataset_model.set_training_dataset(candidate_training_models)
        self.dataset_model.set_validation_dataset(validation_training_models)

    def setup_output_directory(self):
        training_directory = os.path.abspath(self.build["training_set_output_directory"])
        validation_directory = os.path.abspath(self.build["validation_set_output_directory"])

        self.dataset_model.set_training_directory(training_directory)
        self.dataset_model.set_validation_directory(validation_directory)

        self.logger.log("Training set written to: " + str(self.dataset_model.training_directory))
        self.logger.log("Validation set written to: " + str(self.dataset_model.validation_directory))

    def execute(self):
        self.setup_output_directory()
        self.read_in_pickle_files()
