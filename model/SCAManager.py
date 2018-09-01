import numpy as np



'''
SCAManager:

[!!!] 
SCAManager only records the iteration result
and pushes the sca progress, but not assign 
the result. Thus, the input function in the 
funList has to assign the result. 
'''
class SCAManager(object):

    def __init__(self, initValue, funList = [], times = 20, threhold = 0.001):
        self.value = initValue
        self.funcList = funList
        self.times = times
        self.threhold = threhold
        self.itreationResultLists = []


    def _SCA(self):
        if self.itreationResultLists:
            return self.itreationResultLists

        self.itreationResultLists.append(0.0)

        for i in xrange(self.times):
            for fun in self.funcList:
                cur = fun()
            if np.abs(sum(cur) - self.itreationResultLists[-1]) < self.threhold:
                self.itreationResultLists.append(sum(cur))
                break
            self.itreationResultLists.append(sum(cur))

        return self.itreationResultLists

    def execute(self):
        try:
            self._SCA()
            return True
        except:
            return False







