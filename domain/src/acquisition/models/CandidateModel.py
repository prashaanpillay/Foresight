from engine.src.structure.model.Model import Model
from engine.src.utility.assetLoader.ImageUtilities import ImageUtilities
import numpy as np
import os


class CandidateModel(Model):

    def __init__(self):
        self.survey_id = None
        self.output_directory = None

        self.aligned_image_path = None
        self.aligned_image = None
        self.transform = None

        self.reference_image_path = None
        self.reference_image = None

        self.misaligned_image_path = None
        self.misaligned_image = None

        self.candidate_aligned_image = None
        self.candidate_aligned_image_path = None
        self.candidate_transform = None

    def update(self, survey_id, aligned_image, transform, reference_image, misaligned_image):
        self.survey_id = survey_id
        self.transform = transform
        self.aligned_image_path = aligned_image
        self.aligned_image = np.load(aligned_image)
        self.reference_image_path = reference_image
        self.reference_image = np.load(reference_image)
        self.misaligned_image_path = misaligned_image
        self.misaligned_image = np.load(misaligned_image)

    def set_candidate_aligned_image(self, candidate_aligned_image):
        self.candidate_aligned_image = candidate_aligned_image

    def set_candidate_transform(self, candidate_transform):
        self.candidate_transform = candidate_transform

    # measure the error between the aligned_image and the candidate_aligned_image
    def get_accuracy(self):
        return 0

    # determine the variance in the image to determine if any valid image is contained
    def valid_image(self):
        return True

    # write out the images and transforms
    def write_out_given(self, path):
        self.output_directory = path + "\\" + str(self.survey_id)

        self.create_directories_if_absent(self.output_directory)

        self.write_numpy_images(self.output_directory + "\\reference", self.reference_image_path)

        self.write_numpy_images(self.output_directory + "\\misaligned", self.misaligned_image_path)

        self.write_numpy_images(self.output_directory + "\\aligned", self.aligned_image_path)

    def create_directories_if_absent(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

        if not os.path.exists(path + "\\reference"):
            os.mkdir(path + "\\reference")

        if not os.path.exists(path + "\\misaligned"):
            os.mkdir(path + "\\misaligned")

        if not os.path.exists(path + "\\aligned"):
            os.mkdir(path + "\\aligned")

        self.candidate_aligned_image_path = path + "\\candidate"
        if not os.path.exists(self.candidate_aligned_image_path):
            os.mkdir(self.candidate_aligned_image_path)

    def write_numpy_images(self, path, np_array_path):
        if os.path.exists(np_array_path):
            np_array = np.load(np_array_path)
            if len(np_array.shape) == 4:
                # num_images = np_array.shape[3]
                # for i in range(num_images):
                # filename = np_array_path[np_array_path.rfind('\\') + 1:len(np_array_path) - 4] + "_" + str(i)
                filename = np_array_path[np_array_path.rfind('\\') + 1:len(np_array_path) - 4]
                image_array = np_array[0, :, :, 0]
                # ImageUtilities.write_image_from_array(path + "\\" + filename + ".png", image_array)
                ImageUtilities.write_image_from_array(path + "\\" + filename + ".png", image_array)
            elif len(np_array.shape) == 3:
                image_array = np_array[0, :, :]
                filename = np_array_path[np_array_path.rfind('\\') + 1:len(np_array_path) - 4]
                ImageUtilities.write_image_from_array(path + "\\" + filename + ".png", image_array)
