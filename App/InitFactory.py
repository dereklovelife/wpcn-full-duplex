
from RecvBeamModel import *
from SendBeamModel import *
from TimeAllocationModel import *
from model.ResultModel import *
from model.FdWpcn import *
from model.SCAManager import *
from model.ChannelModel import *
from mat.MatalbClient import *

## initial the sum-throughput maximization sca solver
def getSumFDManager(Channel, result):

    beamClient = SumClient()
    client = MatlabClient()
    fdWpcn = SumFdWpcn([])

    ## assemble the sca manager
    ## 1. sendbeam model
    sendModel = SendBeamModel(Channel, result, beamClient)

    ## 2. recvbeam model
    recvModel = RecvBeamModel(Channel, result, beamClient)

    ## 3. time allocation model
    timeModel = TimeAllocationModel(Channel, result, client, fdWpcn)

    ## 4. assemble
    Manager = SCAManager(0, [recvModel.iteartion, timeModel.iteartion, sendModel.iteartion])
    return Manager

## intial the fair-throughput maximization sca solver
def getFairFDManager(Channel, result):
    beamClient = FairClient()
    client = MatlabClient()
    fdWpcn = FairFdWpcn([])

    ## assemble the sca manager
    ## 1. sendbeam model
    sendModel = SendBeamModel(Channel, result, beamClient)

    ## 2. recvbeam model
    recvModel = RecvBeamModel(Channel, result, beamClient)

    ## 3. time allocation model
    timeModel = TimeAllocationModel(Channel, result, client, fdWpcn)

    ## 4. assemble
    Manager = SCAManager(0, [recvModel.iteartion, timeModel.iteartion, sendModel.iteartion])
    return Manager

def getTestFairFDManager(Channel, result):
    beamClient = FairClient()
    client = MatlabClient()
    fdWpcn = FairFdWpcn([])

    ## assemble the sca manager
    ## 1. sendbeam model
    sendModel = SendBeamModel(Channel, result, beamClient)

    ## 2. recvbeam model
    recvModel = RecvBeamModel(Channel, result, beamClient)

    ## 4. assemble
    Manager = SCAManager(0, [recvModel.iteartion, sendModel.iteartion])
    return Manager

def getSumHDManager():
    return None

def getFairHDManager():
    return None

def getSumFDNosiManager():
    return None

def getFairFDNosiManager():
    return None

## initial the result model
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

    ## Small-scale loss of both the UL and the DL is added to the DL
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
    import LogUtil

    os.chdir("D:\wpcn-full-duplex\mat")
    channel = initChannel(2,2, [3,4], 2, 10 ** (-7))

    logger = LogUtil.getLogger(2,2,1)
    result = getInitResultModel(channel, False)

    logger.info("Channel : %s" % channel)
    import copy

    channel2 = copy.copy(channel)
    result2 = copy.copy(result)
    Manager = getSumFDManager(channel, result)
    ret = Manager.execute()
    logger.info("flag: %s, result: %s" % (ret, result))

    print Manager.itreationResultLists

    Manager2 = getFairFDManager(channel2, result2)
    ret = Manager2.execute()
    logger.info("flag: %s, result: %s" % (ret, result2))

    print Manager2.itreationResultLists
