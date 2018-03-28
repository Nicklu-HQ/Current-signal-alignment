from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import numpy as np
import copy

def transpose_path(path):
    path_np = np.array(path)
    path_tr = np.transpose(path_np)
    return path_tr


def path_2_value(x,y,path):
    path_tr  = transpose_path(path)
    value    = copy.copy(path_tr)
    for index,note in enumerate(path_tr[0]):
        value[0][index] = x[note]
    for index,note in enumerate(path_tr[1]):
        value[1][index] = y[note]

    return  path_tr , value


def end_2_end(x,y):
    distance, path = fastdtw(x, y, dist=euclidean)
    #print(distance)
    path, value = path_2_value(x,y,path)
    return path, value












