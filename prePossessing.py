import cv2
import numpy as np


class Img_PrePossessing:
    def __init__(self, image_path):
        self.image_path = image_path

    # image prepossessing method
    def prepossessing(self):
        self.image = self.image_read()
        self.image = self.resize()
        self.image = self.get_grayscale()
        self.image = self.remove_noise()
        self.image = self.thresholding()
        self.image = self.erode()
        return self.image

    # reading image
    def image_read(self):
        return cv2.imread(self.image_path)

    # resize image
    def resize(self):
        return cv2.resize(self.image, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

    # get grayscale image
    def get_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(self):
        return cv2.medianBlur(self.image, 5)

    # thresholding
    def thresholding(self):
        return cv2.threshold(cv2.bilateralFilter(self.image, 3, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # erosion
    def erode(self):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.erode(self.image, kernel, iterations=1)
