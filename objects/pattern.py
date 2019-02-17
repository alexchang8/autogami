import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage.feature import corner_harris, corner_peaks
from sklearn.cluster import DBSCAN

class Pattern:

    def __init__(self, name, dims, creases):
        self.creases = creases
        self.name = name
        self.dims = dims

    def from_image(self, img):
        #lillian
        pass


    def save():
        pass




