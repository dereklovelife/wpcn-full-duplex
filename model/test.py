import numpy as np

from model.binarySearch import binarySearch

gamma = np.linspace(10, 100)
y = np.ones(len(gamma))

class result(object):

    def setX(self, r):
        self.r = r

    def fun(self, x):
        return np.log(1 + x) - x / (1 + x) - self.r - 5.0 / (1 + x)


res = result()
bs = binarySearch(0, 100000000, res.fun)
for i in range(len(gamma)):
    res.setX(gamma[i])
    bs.setFunction(res.fun)
    y[i] = bs.getResult()
    y[i] = np.log(1 + y[i]) - y[i] / (1 + y[i])



