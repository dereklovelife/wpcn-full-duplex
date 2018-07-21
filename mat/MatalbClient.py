import matlabStarter

'''
interact with the matlab.
Call the matlab function.
'''


class MatlabClient(object):
    def __init__(self):
        self.engine = matlabStarter.getEngine()

    def sumSendBeamOptimiztion(self, t, Sr, Hu, Hd, Hsi):
        return self.engine.findSt(t, Sr, Hu, Hd, Hsi, nargout=2)

    def sumRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        return self.engine.findSr(t, St, Hu, Hd, Hsi, nargout=2)

    def fairSendBeamOptimization(self, t, Sr, Hu, Hd, Hsi):
        return self.engine.fairFindSt(t, Sr, Hu, Hd, Hsi, nargout=2)

    def fairRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        return self.engine.fairFindSr(t, St, Hu, Hd, Hsi, nargout=2)

    def getGamma(self, St, Sr, Hu, Hd):
        return self.engine.getGamma(St, Sr, Hu, Hd, nargout = 2)

    def InitChannel(self, k, Nt):
        return self.engine.InitChannel(k, Nt, nargout = 1)

    def BeamInit(self, Hd):
        return self.engine.InitSt(Hd, nargout = 1)


# base client
class BaseClient(object):

    def getSendBeam(self,t, Sr, Hu, Hd, Hsi):
        raise Exception("Unsupport.")

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        raise Exception("Unsupport.")

# client for sum
class SumClient(BaseClient):
    def __init__(self, client):
        self.client = MatlabClient()

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.sumSendBeamOptimiztion(t, Sr, Hu, Hd, Hsi)

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        return self.client.sumRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)

# client for fair
class FairClient(BaseClient):
    def __init__(self, client):
        self.client = MatlabClient()

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.fairSendBeamOptimization(t, Sr, Hu, Hd, Hsi)

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        return self.client.fairRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)
