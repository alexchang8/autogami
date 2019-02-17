import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage.feature import corner_harris, corner_peaks
from sklearn.cluster import DBSCAN
from pattern import Pattern
from crease import Crease


class PatternLoader:

    def __init__(self, load_directory, ksize = 4, pvote = 5, cvote = 18, sample_num = 25):
        self.load_directory = load_directory
        self.ksize = ksize
        self.pvote = pvote
        self.cvote = cvote
        self.sample_num = sample_num


    def isSegment(self, p1,p2, bin_im, ksize, sample_num, pvote, cvote):
        x1, y1 = p1
        x2, y2 = p2
        
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        
        x_disp = abs(x2 - x1)
        y_disp = abs(y2 - y1)
        
        x_step = x_disp / (sample_num + 1)
        y_step = y_disp / (sample_num + 1)
        
        vote = 0
        xstart = 0
        ystart = 0
        
        if x2 >= x1:
            xstart = x1
            ystart = y1
            if y2 < y1:
                y_step = -y_step
        else:
            xstart = x2
            ystart = y2
            if y2 > y1:
                y_step = -y_step

        for mult in range(1, sample_num + 1):  
            
            xc, yc = int(xstart + mult*x_step), int(ystart + mult*y_step)
            view = bin_im[xc - ksize: xc + ksize, yc - ksize: yc + ksize]
             
            if np.sum(view) >= pvote:
                vote += 1 

        return vote >= cvote

    def getCorners(self, img):   
        gray = np.float32(img)
        dst = cv2.cornerHarris(gray,2,3,0.04)
        ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
        dst = np.uint8(dst)
        ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
        corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
        dst = cv2.dilate(dst,None)

        return corners

    def getSegments(self, img, corners, ksize, sample_num, pvote, cvote):
        segment = []
        for i in range(len(corners)):
            for j in range(i+1,len(corners)):
                c1,c2 = tuple(corners[i]), tuple(corners[j])
                if self.isSegment(c1, c2, img, ksize, sample_num, pvote, cvote): 
                    segment.append((c1,c2))
        
        return segment

    def pointCluster(self, points):
        clusters = DBSCAN(eps=6, min_samples=2).fit(points)
        
        labels = clusters.labels_#classes (integers)
        comp = points
        
        labelSum = {}
        for i, l in enumerate(labels):
            
            point = comp[i]
            c = 0
            n = (0.0, 0.0)

            if l == -1:
                labelSum[-1 * i] = (comp[i], 1)  
            if l in labelSum:
                n, c = labelSum.get(l)
            
            c+=1     
            nn = (point[0] + n[0], point[1] + n[1])
            labelSum[l] = (nn, c)
        
        corners = []
        for label, t in labelSum.items():
            center = (int(t[0][0] / t[1]), int(t[0][1] / t[1]))
            corners.append(center)
        return corners

    def getFinalSegments(self,im): #mutates im
        im_display = np.zeros(im.shape, dtype = np.uint8)
        im_display.fill(255)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_orig = im.copy()

        #Binarize and invert
        im = np.invert(im)
        im[im > 10] = 1
        im[im != 1] = 0

        corners = corner_peaks(corner_harris(im_orig, k=0.2))
        corners = self.pointCluster(corners)
        segments = self.getSegments(im, corners, ksize = self.ksize, sample_num = self.sample_num, pvote = self.pvote, cvote = self.cvote)

        w, h = im.shape

        final_seg = []
        for c1,c2 in segments:
            x1,y1 = c1
            x2,y2 = c2
            if not(( x1<10 and x2<10) or (x1>w-10 and x2>w-10) or (y1 < 10 and y2 < 10) or (y1>h-10 and y2>h-10)):
                final_seg.append((c1, c2))

        return final_seg

    def loadPattern(self, file):
        im = cv2.imread(self.load_directory + file)
        segments = self.getFinalSegments(im)

        creases = []
        dims = im.shape[:2]

        for s in segments:
            c = Crease(s[0], s[1])
            creases.append(c)

        return Pattern(file, dims, creases)




        
        
