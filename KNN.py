import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import mode

# Counter.most_common(n): return the most common n items

trainfile = "/Users/chenyimeng/Documents/courses/Data mining/hw3/Iris_train.txt"
testfile = "/Users/chenyimeng/Documents/courses/Data mining/hw3/Iris_test.txt"

numK = 3

class Data_set(object):
    def __init__(self, file):
        self.coor = np.loadtxt(file, delimiter=',', usecols=(0,1,2,3), dtype=float)
        self.label = np.loadtxt(file, delimiter=',', usecols=(4,), dtype=str)

class Test_Data(Data_set):
    testlabel = []

def get_distance(x1, set):
    return np.sqrt((set - x1)**2).sum(1)

def find_minK(distance, k):
    id = np.argsort(distance)
    return id[0:k]

def get_label(test_set, train_set, k, accuracy=False):
    for pt in test_set.coor:
        distance = get_distance(pt, train_set.coor)
        id = find_minK(distance, k)
        nbh_labels = train_set.label[id]
        label = mode(nbh_labels).mode[0]
        test_set.testlabel.append(label)
    if accuracy == True:
        right = []
        n = len(test_set.label)
        for i in range(n):
            right.append(test_set.testlabel[i] == test_set.label[i])
        grade = sum(right) / float(n)
        return grade

train_set = Data_set(trainfile)
test_set = Test_Data(testfile)
print get_label(test_set, train_set, numK, accuracy=True)
print test_set.testlabel