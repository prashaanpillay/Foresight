from engine.src.structure.command.Command import Command
from engine.src.utility.assetLoader.AssetLoader import AssetLoader
from engine.src.utility.logger.Logger import Logger
from engine.src.utility.parsers.JsonParser import JsonParser
from engine.src.model.DatasetModel import DatasetModel

import wget
import os
import shutil
import zipfile


class RetrieveDatasetCommand(Command):

    def execute(self):
        logger = self.injector.get_instance(Logger)
        dataset_model = self.injector.get_instance(DatasetModel)
        assetLoader = self.injector.get_instance(AssetLoader)
        acquisition_config = JsonParser.decode(
            assetLoader.get_config('acquisition.json'))

        dataset = acquisition_config['dataset']
        dataset_url = dataset["download_url"]

        raw_directory = os.path.abspath("assets/raw_set/")
        build = acquisition_config['build']
        training_directory = os.path.abspath(
            build["training_set_output_directory"])
        validation_directory = os.path.abspath(
            build["validation_set_output_directory"])

        dataset_model.set_training_directory(training_directory)
        dataset_model.set_validation_directory(validation_directory)

        if not (os.path.exists(training_directory) and os.path.exists(validation_directory)) and (not os.path.exists(raw_directory)) :
            logger.log("Downloading dataset")
            url_name = wget.download(dataset_url, raw_directory)
            with zipfile.ZipFile(url_name, 'r') as zip_ref:
                zip_ref.extractall(raw_directory)

            shutil.copytree(
                raw_directory+dataset["training_set_input_directory"], training_directory)

            shutil.copytree(
                raw_directory+dataset["validation_set_input_directory"], validation_directory)

            logger.progress("Dataset download complete")

        else: 
            if os.path.exists(raw_directory):
                if build["clear_out_folders_before_run"]:
                    logger.warn("Clearing out previous training and validation directories")
                    shutil.rmtree(training_directory)
                    shutil.rmtree(validation_directory)
                    
                shutil.copytree(
                    raw_directory+dataset["training_set_input_directory"], training_directory)

                shutil.copytree(
                    raw_directory+dataset["validation_set_input_directory"], validation_directory)

                logger.progress("Dataset download complete")

        logger.log("Training set written to: " +
                   str(dataset_model.training_directory))
        logger.log("Validation set written to: " +
                   str(dataset_model.validation_directory))
