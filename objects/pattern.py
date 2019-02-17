import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage.feature import corner_harris, corner_peaks
from sklearn.cluster import DBSCAN

from gcode import Gcode
from crease import Crease

class Pattern:

    def __init__(self, name, dims, creases):
        self.creases = creases
        self.name = name
        self.dims = dims


    def save_to_txt(self, fp, name):

        g = Gcode(name, self).to_string_list()

        with open(fp + name + '.txt', 'w') as f:
            for line in g:
                f.write("%s\n" % line)
        return None

    def load_from_txt(self, fp, name):
        with open(fp + name + '.txt', 'w') as f:
            lines = f.readlines()

        creases = []
        dims = ines[0].split(" ")
        for l in lines[1:]:
            a,b,c,d = l.split(" ")
            creases.append(Crease(a,b,c,d))

        return Pattern(name, dims, creases)

    def load_from_string(self, name, s):
        lines = s.split("\n")

        dims = lines[0].split(" ")
        print(dims)

        nd = []
        for d in dims:
            nd.append(int(d))


        creases = []
        for l in lines[1:]:
            if l == '':
                continue
            print(l.split(" "))
            a,b,c,d = l.split(" ")
            creeee = Crease((a,b),(c,d)).intyboi()
            print(creeee)
            creases.append(creeee)


        return Pattern(name, nd, creases)






