import numpy as np

class KdTree:
    def __init__(self, k=1) -> None:
        self.k = k
        # preparatories: [(ele_list, val, used)]
        # used: 0/1
        self.preparatories = []
    
    def _reset(self):
        self.__init__(self.k)

    def kd(self, vector: np.ndarray):
        self.length = vector.shape[0]
        


    def _factorial(self, n):
        fact = 1
        if n < 0:
            raise 'n is wrong'
        elif n == 0:
            return 1
        else:
            for i in range(1, n+1):
                fact = fact * i
            return fact

    def _make_preparatories(self, num):
        pass