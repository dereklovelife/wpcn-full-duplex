import matlabStarter
import matlab

'''
interact with the matlab.
Call the matlab function.
'''


class MatlabClient(object):
    def __init__(self):
        self.engine = matlabStarter.getEngine()

    def sumSendBeamOptimiztion(self, t, Sr, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.findSt(t, Sr, Hu, Hd, Hsi, nargout=2)

    def sumRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        tt = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.findSr(tt, St, Hu, Hd, Hsi, nargout=2)

    def fairSendBeamOptimization(self, t, Sr, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.fairFindSt(t, Sr, Hu, Hd, Hsi, nargout=2)

    def fairRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.fairFindSr(t, St, Hu, Hd, Hsi, nargout=2)

    def getGamma(self, St, Sr, Hu, Hd):
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.getGamma(St, Sr, Hu, Hd, nargout = 1)

    def InitChannel(self, k, Nt):
        return self.engine.InitChannel(k, Nt, nargout = 1)

    def BeamInit(self, Hd, flag = True):
        if flag:
            return self.engine.InitSt(Hd, nargout = 1)
        else:
            return self.engine.InitSt2(Hd, nargout = 1)


# base client
class BaseClient(object):

    def getSendBeam(self,t, Sr, Hu, Hd, Hsi):
        raise Exception("Unsupport.")

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        raise Exception("Unsupport.")

# client for sum
class SumClient(BaseClient):
    def __init__(self):
        self.client = MatlabClient()

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.sumSendBeamOptimiztion(t, Sr, Hu, Hd, Hsi)

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        return self.client.sumRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)

# client for fair
class FairClient(BaseClient):
    def __init__(self):
        self.client = MatlabClient()

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.fairSendBeamOptimization(t, Sr, Hu, Hd, Hsi)

    def getRecvBeam(self,t, Sr, Hu, Hd, Hsi):
        return self.client.fairRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)



