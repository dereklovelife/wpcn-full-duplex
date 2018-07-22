
from RecvBeamModel import *
from SendBeamModel import *
from TimeAllocationModel import *
from model.ResultModel import *
from model.FdWpcn import *
from model.SCAManager import *
from model.ChannelModel import *
from mat.MatalbClient import *


def getSumFDManager(Channel, result):

    beamClient = SumClient()
    client = MatlabClient()
    fdWpcn = SumFdWpcn([])
    sendModel = SendBeamModel(Channel, result, beamClient)
    recvModel = RecvBeamModel(Channel, result, beamClient)
    timeModel = TimeAllocationModel(Channel, result, client, fdWpcn)
    Manager = SCAManager(0, [recvModel.iteartion, timeModel.iteartion, sendModel.iteartion])
    return Manager

def getFairFDManager(Channel, result):
    beamClient = FairClient()
    client = MatlabClient()
    fdWpcn = FairFdWpcn([])
    sendModel = SendBeamModel(Channel, result, beamClient)
    recvModel = RecvBeamModel(Channel, result, beamClient)
    timeModel = TimeAllocationModel(Channel, result, client, fdWpcn)
    Manager = SCAManager(0, [recvModel.iteartion, timeModel.iteartion, sendModel.iteartion])
    return Manager

def getSumHDManager():
    return None

def getFairHDManager():
    return None

def getSumFDNosiManager():
    return None

def getFairFDNosiManager():
    return None

def getInitResultModel(Channel, flag = True):
    userNum = len(Channel.Hu)
    resultModel = ResultModel()
    resultModel.t = [1.0 / (userNum + 1)] * (userNum + 1)
    resultModel.userOrder = range(userNum)
    resultModel.sendBeam = MatlabClient().BeamInit(Channel.Hd, flag)
    return resultModel

def _getInitChannel(k, Nt):
    return MatlabClient().InitChannel(k, Nt)

def initChannel(k, Nt, d1, alpha, pNoise):
    Hd = _getInitChannel(k, Nt)
    Hu = _getInitChannel(k, Nt)
    Hsi = _getInitChannel(Nt, Nt)
    for i in range(len(Hd)):
        for j in range(len(Hd[i])):
            realpart = Hd[i][j].real
            imagpart = Hd[i][j].imag
            realpart *= np.sqrt(d1[i] ** (-alpha) / pNoise * 10 ** (-2))
            imagpart *= np.sqrt(d1[i] ** (-alpha) / pNoise * 10 ** (-2))
            Hd[i][j] = complex(realpart, imagpart)

    return ChannelModel(Hu, Hd, Hsi)


if __name__ == "__main__":
    import os
    os.chdir("D:\wpcn-full-duplex\mat")
    channel = initChannel(2,2, [3,4], 2, 10 ** (-7))

    result = getInitResultModel(channel, False)

    import copy
    channel2 = copy.copy(channel)
    result2 = copy.copy(result)

    Manager = getSumFDManager(channel, result)
    ret = Manager.execute()

    Manager2 = getFairFDManager(channel2, result2)
    ret = Manager2.execute()
