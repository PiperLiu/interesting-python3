from kdTree import KdTree
import numpy as np

kt = KdTree()

a = [0.4, 0.1, 0.6]
a = np.asfarray(a)

kt.kd(a)