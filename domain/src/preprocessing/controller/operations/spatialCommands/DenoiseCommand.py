from ..PreprocessingCommand import PreprocessingCommand
import cv2 as cv


class DenoiseCommand(PreprocessingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, imagePath):
        super().execute(imagePath)
        print(imagePath)
        blurredImage = cv.equalizeHist(self.image)
        cv.imwrite(imagePath, blurredImage)
