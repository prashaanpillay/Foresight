
from ..PreprocessingCommand import PreprocessingCommand
import cv2 as cv
import ray

@ray.remote
class GrayscaleCommand(PreprocessingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, imagePath):        
        super().execute(imagePath)
        grayscale = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
        cv.imwrite(imagePath, grayscale)
        # TODO: have some way of setting a global tracking mechanism for input channels
