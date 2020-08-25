from engine.src.structure.command.Command import Command
from skimage import io


class PreprocessingCommand(Command):
    
    def __init__(self):
        self.image = None

    def execute(self, imagePath):
        super().execute()
        self.image = io.imread(imagePath)