from engine.src.structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from engine.src.utility.logger.Logger import Logger
from engine.src.structure.injector.Injector import Injector
from pathlib import Path

import tensorflow as tf
import os


class FilterOutCorruptedImagesCommand(Command):

    def execute(self):
        logger = self.injector.get_instance(Logger)
        dataset_model = self.injector.get_instance(DatasetModel)

        paths = list(Path(dataset_model.training_directory).rglob('*.jpg'))

        num_skipped = 0
        for fpath in paths:
            try:
                fobj = open(fpath, "rb")
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                # Delete corrupted image
                os.remove(fpath)
                self.logger.warn("Removed: "+fpath)

        print("Deleted %d images" % num_skipped)
