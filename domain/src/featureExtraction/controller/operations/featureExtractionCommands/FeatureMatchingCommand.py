from engine.src.structure.command.Command import Command
import cv2 as cv


class FeatureMatchingCommand(Command):

    def __init__(self):
        self.image = None

    def execute(self, candidate_model):
        super().execute()

        image_path_1 = candidate_model.output_directory + "\\misaligned\\" + candidate_model.misaligned_image_path[candidate_model.misaligned_image_path.rfind('\\') + 1:len(candidate_model.misaligned_image_path) - 4] + ".png"
        image_path_2 = candidate_model.output_directory + "\\reference\\" + candidate_model.reference_image_path[candidate_model.reference_image_path.rfind('\\') + 1:len(candidate_model.reference_image_path) - 4] + ".png"

        self.image1 = cv.imread(image_path_1)
        self.image2 = cv.imread(image_path_2)
