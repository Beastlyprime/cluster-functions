import numpy as np
from collections import Counter

filename = "/Users/chenyimeng/Documents/courses/Data mining/hw3/Iris_train.txt"

changes = 10

class Point(object):
    def __init__(self, coor, label, id=-1):
        self.coor = coor
        self.label = label
        self.id = id

# a cluster
class kmeans_center(object):
    def __init__(self, coor, id):
        # the coordinate of its center
        self.coor = coor
        # the coordinates of all the pts in it
        self.members = []
        # the label of all the pts in it
        self.label = []
        # the number of pts in it
        self.num = 0.
        self.id = id

    # get a new point into this cluster
    def get_in(self, new_point):
        global changes
        self.members.append(new_point.coor)
        self.label.append(new_point.label)
        self.num += 1
        if new_point.id != self.id:
            new_point.id = self.id
            changes += 1
        return new_point

    def get_label(self):
        return Counter(self.label).most_common(1)[0][0]

# k clusters
class K_clusters(object):
    def __init__(self, x, center_num=5):
        self.nparray = x
        self.center_num = center_num
        self.centers = [] # the list of kmeans_center. id is responding to that.

    # choose k centers randomly
    def initial(self):
        nsample, nfeature = self.nparray.shape
        center_id = []
        for i in range(self.center_num):
            new_id = np.random.randint(0, nsample)
            while new_id in center_id:
                new_id = np.random.randint(0, nsample)
            center_id.append(new_id)
            new_center = kmeans_center(self.nparray[new_id,0:4], i)
            self.centers.append(new_center)

    def restart(self):
        for center in self.centers:
            center.coor = np.array(center.members).sum(0) / len(center.members)
            center.num = 0.
            center.label = []
            center.members = []

# return the id of the nearest cluster to a point
def min_distance(centers, cand_point):
    coors = []
    for center in centers.centers:
        coors.append(center.coor)
    dist = np.square(coors-cand_point.coor).sum(1)
    min_id = np.where(dist == np.min(dist))
    return min_id[0]

def K_means(filename, cluster_num):
    global changes
    # init
    label = []
    points_list = []
    data_coor = np.loadtxt(filename, usecols=(0, 1, 2, 3), dtype=float, delimiter=',')
    data_label = np.loadtxt(filename, usecols=(4,), dtype=str, delimiter=',')

    # change str into float, for the convenience of computing
    all_label = Counter(list(data_label)).keys()
    for i in range(len(all_label)):
        data_label[data_label == all_label[i]] = i
    data_label = data_label.astype(float)
    x = np.block([data_coor,data_label.reshape((-1,1))])

    # init clusters
    clusters = K_clusters(x, center_num=cluster_num)
    clusters.initial()
    for pt in x:
        point = Point(pt[0:4], label=pt[4])
        points_list.append(point)
    init = 1

    # do k-means
    while changes > 5:
        changes = 0
        if init == 0:
            clusters.restart()
        for i, point in enumerate(points_list):
            min_id = min_distance(clusters, point)
            points_list[i] = clusters.centers[min_id[0]].get_in(point)
        init = 0

    # get label
    for center in clusters.centers:
        label.append(center.get_label())
    for point in points_list:
        point.label = label[point.id]

    # compute the precision
    acc = 0.
    for point in points_list:
        for i in range(len(data_coor)):
            if cmp(list(data_coor[i]),list(point.coor)) == 0:
                j = i
                break
        if data_label[j] == point.label:
            acc += 1.
    print "precision = ", acc/len(data_coor)

    # print the result
    for point in points_list:
        print point.coor, all_label[int(point.label)], point.id

K_means(filename, cluster_num=10)