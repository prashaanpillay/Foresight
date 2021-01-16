from engine.src.structure.model.Model import Model
from engine.src.utility.assetLoader.ImageUtilities import ImageUtilities
import numpy as np
import os


class CandidateModel(Model):

    def __init__(self):
        self.survey_id = None

        self.aligned_image = None
        self.transform = None

        self.reference_image = None
        self.misaligned_image = None

        self.candidate_aligned_image = None
        self.candidate_transform = None

    def update(self, survey_id, aligned_image, transform, reference_image, misaligned_image):
        self.survey_id = survey_id
        self.aligned_image = aligned_image
        self.transform = transform
        self.reference_image = reference_image
        self.misaligned_image = misaligned_image

    def set_candidate_aligned_image(self, candidate_aligned_image):
        self.candidate_aligned_image = candidate_aligned_image

    def set_candidate_transform(self, candidate_transform):
        self.candidate_transform = candidate_transform

    # measure the error between the aligned_image and the candidate_aligned_image
    def get_accuracy(self):
        return 0

    # write out the images and transforms
    def write_out(self, path):
        directory_to_create = path+"\\"+str(self.survey_id)
        if not os.path.exists(directory_to_create):
            os.mkdir(directory_to_create)

            os.mkdir(directory_to_create+"\\reference")
            self.write_numpy_images(directory_to_create +
                                    "\\reference", self.reference_image)

            os.mkdir(directory_to_create+"\\misaligned")
            self.write_numpy_images(directory_to_create +
                                    "\\misaligned", self.misaligned_image)

            os.mkdir(directory_to_create+"\\aligned")
            self.write_numpy_images(directory_to_create +
                                    "\\aligned", self.aligned_image)
        else:
            pass
            # iterate through the images and them out

    def write_numpy_images(self, path, array):
        if os.path.exists(array):
            np_array = np.load(array)
            if len(np_array.shape) == 4:
                num_images = np_array.shape[3]
                for i in range(num_images):
                    image_array = np_array[0, :, :, i]
                    ImageUtilities.write_image_from_array(
                        path+"\\"+str(i)+".png", image_array)
            elif len(np_array.shape) == 3:
                image_array = np_array[0, :, :]
                ImageUtilities.write_image_from_array(
                    path+"\\"+"1.png", image_array)
        else:
            print(array)
