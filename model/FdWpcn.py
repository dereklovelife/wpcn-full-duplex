import numpy as np

from model.binarySearch import binarySearch

BINARY_SEARCH_START = 0.0
BINARY_SEARCH_END = 1000000.0


class FdWpcnBase(object):
    def __init__(self, gain):
        # channel gain
        self.gain = gain

        # number of ue
        self.ueCount = len(gain)

        self.flag = 2 ** (self.ueCount) - 1
        # dp map
        # init 0
        self.dpMap = {0: 0.0}

        # record the user position
        self.usTraceMap = {}

        # recorde variable z
        self.zTraceMap = {}

        # isDone
        self.isDone = False

        # timeList
        self.timeList = []

        # userOrder
        self.userOrder = []

        # throughput
        self.throughput = []

        # zList sorted
        self.zList = []
    # dp to determine the user schedule.
    # flag: the left user set
    def dp(self, flag):
        if flag in self.dpMap:
            return self.dpMap[flag]

        tmpFlag = flag

        maxTmp = -1
        maxIndex = -1
        maxZ = -1
        for i in range(self.ueCount):
            base = 1 << i

            if tmpFlag & base:
                # ue_i is in the left user set

                cur,z = self.getThroughput(tmpFlag, i, base)

                if cur > maxTmp:
                    maxTmp = cur
                    maxIndex = i
                    maxZ = z

        self.usTraceMap.update({flag: maxIndex})
        self.dpMap.update({flag: maxTmp})
        self.zTraceMap.update({flag: maxZ})
        return self.dpMap[flag]

    # sub-class override
    def getThroughput(self, tmpFlag, i, base):
        raise Exception("Unsupport.")

    # return throughput
    def getThroughputResult(self):
        return self.dp(self.flag)

    # get the user position
    def getUserPositionResult(self):
        # check dp done
        if self.userOrder:
            return self.userOrder
        flag = self.flag
        while flag:
            nt = self.usTraceMap[flag]
            self.userOrder.append(nt)
            self.zList.append(self.zTraceMap[flag])
            flag -= 2 ** nt

        # need reverse
        self.userOrder.reverse()
        return self.userOrder

    # set gain
    def setGain(self, gain):
        self.gain = gain

        # initial all the records
        self.dpMap = {0: 0.0}
        self.usTraceMap = {}
        self.zTraceMap = {}
        self.isDone = False
        self.timeList = []
        self.userOrder = []
        self.throughput = []
        self.zList = []

    def getTime(self):
        if not self.zList:
            self.getUserPositionResult()

        if self.timeList:
            return self.timeList
        leftTime = 1.0
        for i in self.zList:
            t2 = leftTime / (1 + i)
            self.timeList.append(t2)
            leftTime -= t2
        self.timeList.append(leftTime)
        self.timeList.reverse()
        return self.timeList

    def getTh(self):
        if not self.timeList:
            self.getTime()
        for i in xrange(len(self.timeList) - 1):
            self.throughput.append(self.timeList[i + 1] * np.log(1 + self.gain[self.userOrder[i]] * self.zList[-i-1]))
        return self.throughput


# express for sumThroughput bianry search
class SumExpress(object):
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def fun(self, x):
        return np.log(1 + x) - x / (1 + x) - self.r1 - self.r2 / (1 + x)


# express for fairThroughput bianry search

class FairExpress(object):
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def fun(self, x):
        return self.r1 * x - np.log(1 + self.r2 * x)


# handle the sum-throughput maximization
class SumFdWpcn(FdWpcnBase):
    def getThroughput(self, tmpFlag, i, base):
        r1 = self.dp(tmpFlag - base)
        r2 = self.gain[i]

        # binary search
        eps = SumExpress(r1, r2)
        bs = binarySearch(0, BINARY_SEARCH_END, eps.fun)
        x = bs.getResult()

        return np.log(1 + x) - x / (1 + x), x/r2




# handle the fair-throughput maximization
class FairFdWpcn(FdWpcnBase):
    def getThroughput(self, tmpFlag, i, base):
        r1 = self.dp(tmpFlag - base)
        r2 = self.gain[i]

        ## handle single user situation
        if r1 == 0.0:

            ## single user use sum-throughput expression
            eps = SumExpress(r1, r2)
            bs = binarySearch(0, BINARY_SEARCH_END, eps.fun)
            x = bs.getResult()
            return np.log(1 + x) - x / (1 + x), x

        if r2 < r1:
            return 0.0, 1.0
        eps = FairExpress(r1, r2)
        bs = binarySearch(0, BINARY_SEARCH_END, eps.fun)

        x = bs.getResult()
        return r1 * x / (1 + x), x



if __name__ == "__main__":
    # gain = np.abs(np.random.rand(4) * 10)

    gain = [79, 65, 95, 50, 44, 23, 9, 300]
    obj = SumFdWpcn(gain)
    print(obj.getThroughputResult())
    print(obj.getUserPositionResult())
    print(sum(obj.getTh()))
    print(len(obj.getTime()))
