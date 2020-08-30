
from .PreprocessingCommand import PreprocessingCommand
import cv2 as cv


class AveragingBlurCommand(PreprocessingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, imagePath):        
        super().execute(imagePath)
        averageBlurredImage = cv.blur(self.image,(5,5))
        cv.imwrite(imagePath, averageBlurredImage)
