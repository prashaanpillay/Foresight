from engine.src.structure.command.Command import Command
import cv2 as cv


class PreprocessingCommand(Command):
    
    def __init__(self):
        self.image = None

    def execute(self, imagePath):
        super().execute()        
        self.image = cv.imread(imagePath, cv.IMREAD_UNCHANGED)