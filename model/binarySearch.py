

class binarySearch(object):

    def __init__(self, start = 0, end = 1, function = None, threhold = 0.0001):
        self.start = start
        self.end = end
        self.function = function
        self.threhold = threhold

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def setFunction(self, fun):
        self.function = fun

    def getResult(self):

        if not self.function:
            return -1

        start = self.start
        end = self.end

        while end - start > 0.001:
            mid = (start + end) * 0.5
            if self.function(mid) > 0:
                end = mid
            else:
                start = mid

        return start
