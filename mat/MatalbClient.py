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

    def sumHdOptimization(self, Hu, Hd, Hsi):
        return self.engine.sumThHD(Hu, Hd, Hsi, nargout = 2)

    def fairHdOptimization(self, Hu, Hd, Hsi):
        return self.engine.fairHD(Hu, Hd, Hsi, nargout = 2)

    def sumNosiSendBeamOptimization(self, t, Sr, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.findSt_nosi(t, Sr, Hu, Hd, Hsi, nargout=2)

    def sumNosiRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        tt = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.findSr_nosi(tt, St, Hu, Hd, Hsi, nargout=2)

    def fairNosiSendBeamOptimization(self, t, Sr, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.fairFindSt_nosi(t, Sr, Hu, Hd, Hsi, nargout=2)

    def fairNosiRecvBeamOptimization(self, t, St, Hu, Hd, Hsi):
        t = matlab.double(t)
        Hu = matlab.double(Hu, is_complex=True)
        Hd = matlab.double(Hd, is_complex=True)
        return self.engine.fairFindSr_nosi(t, St, Hu, Hd, Hsi, nargout=2)

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



class SumNosiClient(BaseClient):

    def __init__(self):
        self.client = MatlabClient()

    def getRecvBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.sumNosiRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.sumNosiSendBeamOptimization(t, Sr, Hu, Hd, Hsi)

class FairNosiClient(BaseClient):

    def __init__(self):
        self.client = MatlabClient()

    def getRecvBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.fairNosiRecvBeamOptimization(t, Sr, Hu, Hd, Hsi)

    def getSendBeam(self, t, Sr, Hu, Hd, Hsi):
        return self.client.fairNosiSendBeamOptimization(t, Sr, Hu, Hd, Hsi)


class HdClient(object):

    def __init__(self):
        self.client = MatlabClient()

    def sumth(self, Hu, Hd, Hsi):
        return self.client.sumHdOptimization(Hu, Hd, Hsi)

    def fairth(self, Hu, Hd, Hsi):
        return self.client.fairHdOptimization(Hu, Hd, Hsi)

