
from ..PreprocessingCommand import PreprocessingCommand
import cv2 as cv
import ray


@ray.remote
class BlurCommand(PreprocessingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, imagePath):
        super().execute(imagePath)
        blurredImage = cv.blur(self.image, (5, 5))
        cv.imwrite(imagePath, blurredImage)
