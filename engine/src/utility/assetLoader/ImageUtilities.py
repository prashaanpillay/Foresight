import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os


class ImageUtilities:

    @staticmethod
    def read_image(image_path):
        image_array = None
        if os.path.exists(image_path):
            if image_path.endswith('.npy'):
                image_array = np.load(image_path)

        return image_array

    @staticmethod
    def show_image(image_path):
        data = ImageUtilities.read_image(image_path)
        plt.imshow(data)
        plt.show()

    @staticmethod
    def write_image_from_array(path, array):
        matplotlib.image.imsave(path, array)

    @staticmethod
    def crop(image, random_crop, image_size):
        pass

    @staticmethod
    def flip(image, random_flip):
        pass

    @staticmethod
    def to_rgb(img):
        pass
