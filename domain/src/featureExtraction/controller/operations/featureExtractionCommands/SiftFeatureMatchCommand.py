
from .FeatureMatchingCommand import FeatureMatchingCommand
import numpy as np
import cv2 as cv
from engine.src.utility.assetLoader.ImageUtilities import ImageUtilities


class SiftFeatureMatchCommand(FeatureMatchingCommand):

    def __init__(self):
        super().__init__()

    def execute(self, candidate_model):

        MIN_MATCH_COUNT = 3
        FLANN_INDEX_KDTREE = 1

        orb = cv.SIFT_create()

        super().execute(candidate_model)

        # Now detect the keypoints and compute
        # the descriptors for the query image
        # and train image
        keypoints1, descriptor1 = orb.detectAndCompute(self.image1, None)
        keypoints2, descriptor2 = orb.detectAndCompute(self.image2, None)

        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(descriptor1, descriptor2, k=2)
        # store all the good matches as per Lowe's ratio test.
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) >= MIN_MATCH_COUNT:
            src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()
            h, w = self.image1.shape[:-1]
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv.perspectiveTransform(pts, M)
            self.image2 = cv.polylines(self.image2, [np.int32(dst)], True, 255, 3, cv.LINE_AA)
            candidate_model.set_candidate_aligned_image(self.roi(self.image2, [np.int32(dst)]))
            filename = candidate_model.reference_image_path[candidate_model.reference_image_path.rfind('\\') + 1:len(candidate_model.reference_image_path) - 4]
            ImageUtilities.write_image_from_array(candidate_model.candidate_aligned_image_path + "\\" + filename + ".png", candidate_model.candidate_aligned_image)
        else:
            print("Not enough matches are found for {} - {}/{}".format(candidate_model.reference_image_path, len(good), MIN_MATCH_COUNT))
            matchesMask = None

        # draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
        #                    singlePointColor=None,
        #                    matchesMask=matchesMask,  # draw only inliers
        #                    flags=2)
        # img3 = cv.drawMatches(self.image1, kp1, self.image2, kp2, good, None, **draw_params)
        # plt.imshow(img3), plt.show()

    def roi(self, img, vertices):
        mask = np.zeros_like(img)
        cv.fillPoly(mask, vertices, 255)
        masked = cv.bitwise_and(img, mask)
        return masked
