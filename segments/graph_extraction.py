import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import DBSCAN
from functools import reduce
from itertools import combinations, chain
from toolz.functoolz import pipe

def binarize(img):
    gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dn = cv2.fastNlMeansDenoising(gray2, None, 10, 7, 21)
    bin_img = cv2.adaptiveThreshold(dn,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,19,10)
    return bin_img

def get_lines(bin_img):
    lines = cv2.HoughLinesP(bin_img, rho=0.05, theta=0.05*(np.pi/180),
                            threshold = 7, minLineLength = 10, maxLineGap = 5)
    return lines

def p_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def norm(l):
    x1, y1, x2, y2 = l
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def seg_angle(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    dot = (x2 - x1) * (x4 - x3) + (y2 - y1) * (y4 - y3)
    d = dot / (norm(l1) * norm(l2))
    if d < -1:
        d = -1.
    elif d > 1:
        d = 1.
    res = math.degrees(math.acos(d))
    if res > 90:
        res = 180 - res
    return res

def d_to_seg(p, line):
    p1x, p1y, p2x, p2y = line
    p1 = p1x, p1y
    p2 = p2x, p2y
    p3x, p3y = p
    xdelta = p2x - p1x
    ydelta = p2y - p1y
    u = ((p3x - p1x) * xdelta + (p3y - p1y) * ydelta) / \
        (xdelta * xdelta + ydelta * ydelta)
    if u < 0:
        closest = p1
    elif u > 1:
        closest = p2
    else:
        closest = p1x + u * xdelta, p1y + u * ydelta
    return p_dist(closest, p)

def seg_dist(l1, l2):
    d1 = d_to_seg(l1[:2], l2)
    d2 = d_to_seg(l1[2:], l2)
    d3 = d_to_seg(l2[:2], l1)
    d4 = d_to_seg(l2[2:], l1)
    return min(d1, d2, d3, d4)

def similar(l1, l2):
    return 1 if seg_dist(l1, l2) < 5 and seg_angle(l1, l2) < 6 else 100

def merge_lines(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    p1, p2 = (x1, y1), (x2, y2)
    p3, p4 = (x3, y3), (x4, y4)
    dmax = -1
    for a, b in combinations([p1, p2, p3, p4], 2):
        d = p_dist(a, b)
        if d > dmax:
            dmax = d
            res = [a[0], a[1], b[0], b[1]]
    return res

def cluster_lines(lines):
    sq = np.squeeze(lines)
    #minsamples should probably be 1 here
    db = DBSCAN(metric=similar, eps=3., min_samples=2).fit(sq)
    uniq_labels = set(db.labels_)
    label_count = max(uniq_labels) + 1
    labeled = np.fromiter(chain.from_iterable(
                            reduce(merge_lines, sq[db.labels_ == k])
                            for k in range(0, label_count)),
                          dtype = 'int16')
    labeled.shape = -1, 4
    #lines marked as -1
    noise = sq[db.labels_ == -1]
    pruned = np.concatenate([labeled, noise])
    return pruned

def cluster_coordinates(pruned):
    coords = np.reshape(pruned, (-1, 2))
    coord_db = DBSCAN(eps=7., min_samples=2).fit(coords)
    clabels = coord_db.labels_
    max_coord = max(clabels) + 1
    labeled_lines = np.reshape(clabels,(-1, 2))
    clustered_coords = np.fromiter(chain.from_iterable(
                            np.round(np.mean(coords[clabels == k], axis = 0))
                            for k in range(0, max_coord)),
                        dtype = 'int16', count = max_coord * 2)
    clustered_coords.shape = -1, 2
    noise_coords = coords[clabels < 0]
    np.place(clabels, clabels < 0, np.arange(max_coord, max_coord + len(noise_coords)))
    merged_coords = np.concatenate([clustered_coords, noise_coords])
    return merged_coords, labeled_lines

def cluster_axis(merged_coords, axis):
    coords = merged_coords[:, axis]
    coords.shape = -1, 1
    db = DBSCAN(eps=3, min_samples=2).fit(coords)
    labels = db.labels_
    coords = np.squeeze(coords)
    for k in np.nditer(np.arange(max(labels) + 1)):
        coords[np.where(labels == k)] = np.round(np.mean(coords[labels == k]))

def save_img(merged, lines, name, img):
    blank = np.zeros_like(img)
    for a,b in lines:
        (x1, y1), (x2, y2) = merged[a], merged[b]
        color = (np.random.rand() * 255,np.random.rand() * 255,np.random.rand() * 255)
        cv2.line(blank,(x1,y1),(x2,y2),color,1)
        cv2.circle(blank, (x1, y1), 5, color)
        cv2.circle(blank, (x2, y2), 5, color)
    cv2.imwrite(name, blank)

def extract_dict(request):
    img = cv2.imdecode(np.fromstring(request.files['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    # img = cv2.imread('segments/images/butterfly_CP.jpg')
    merged, lines = pipe(img, binarize, get_lines, cluster_lines, cluster_coordinates)
    #cluster y axis
    cluster_axis(merged, 1)
    #cluster x axis
    cluster_axis(merged, 0)
    xcoords, ycoords = merged[:, 0], merged[:, 1]
    xmin, xmax = np.min(xcoords), np.max(xcoords)
    ymin, ymax = np.min(ycoords), np.max(ycoords)
    if xmax > 0 and ymax > 0:
        print("scaling")
        print(xmin, xmax, ymin, ymax)
        merged[:, 0] = np.round(800 * ((xcoords - xmin) / (xmax - xmin)))
        merged[:, 1] = np.round(800 * ((ycoords - ymin) / (ymax - ymin)))
    else:
        merged[:, 0] = np.round(800 * (xcoords / img.shape[0]))
        merged[:, 1] = np.round(800 * (ycoords / img.shape[1]))
    return {"nodes": merged.tolist(), "edges": lines.tolist()}

def main():
    img = cv2.imread('images/crane1.png')
    merged, lines = pipe(img, binarize, get_lines, cluster_lines, cluster_coordinates)
    #cluster y axis
    cluster_axis(merged, 1)
    #cluster x axis
    cluster_axis(merged, 0)
    save_img(merged, lines, "final.png", img)

if __name__ == '__main__':
    main()
