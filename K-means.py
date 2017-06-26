import numpy as np
import pandas as pd

filename = "/Users/chenyimeng/Documents/courses/Data mining/hw3/Iris_train.csv"

data = pd.read_csv(filename)
label = np.array(data['label'])


class kmeans_center(object):
    def __init__(self, coor, label):
        self.coor = coor
        self.label = label

class K_centers(object):
    def __init__(self,x, center_num=5):
        self.nparray = x
        self.center_num = center_num
        self.centers = []
    def initial(self):
        nsample, nfeature = self.nparray.shape
        center_id = []
        for i in range(self.center_num):
            new_id = np.random.randint(0, nsample)
            while new_id in center_id:
                new_id = np.random.randint(0, nsample)
            center_id.append(new_id)
            new_center = kmeans_center(self.nparray[new_id,0:4],self.nparray[new_id,4])
            print new_center.coor
            self.centers.append(new_center)

def min_distance(centers, cand_point):
    dist = np.square(centers-cand_point)
    min_id = np.where(dist == np.min(dist))
    return centers[min_id]

def means_cluster(centers, point):
    pass

def K_means(x):
    label = np.zeros(len(x))
    features = x[:, 0:4]
    new_centers = K_centers(x, center_num=5)
    rest = features.remove(new_centers.centers)
    ###
    for point in rest:
        centers = new_centers
        new_centers, label = means_cluster(centers, point)
    return label
