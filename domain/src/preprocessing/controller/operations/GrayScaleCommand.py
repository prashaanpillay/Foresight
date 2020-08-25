
from .PreprocessingCommand import PreprocessingCommand
from skimage import io
from skimage.color import rgb2gray
from skimage import img_as_ubyte


class GrayscaleCommand(PreprocessingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, imagePath):        
        super().execute(imagePath)
        grayscale = rgb2gray(self.image)
        io.imsave(imagePath, img_as_ubyte(grayscale))
