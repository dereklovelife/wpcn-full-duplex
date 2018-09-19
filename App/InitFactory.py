
from RecvBeamModel import *
from SendBeamModel import *
from TimeAllocationModel import *
from mat.MatalbClient import *
from model.fd.FdWpcn import *
from model.util.ChannelModel import *
from model.util.ResultModel import *
from model.util.SCAManager import *
from model.util.BaseManager import *


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

def getSumHDManager(Channel, result):
    return SumHdManager(HdClient(), Channel, result)

def getFairHDManager(Channel, result):
    return FairHdManager(HdClient(), Channel, result)

def getSumFDNosiManager(Channel, result):
    beamClient = SumNosiClient()
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

def getFairFDNosiManager(Channel, result):
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
    # Hu = _getInitChannel(k, Nt)
    Hu = copy.deepcopy(Hd)
    Hsi = _getInitChannel(Nt, Nt)

    ## Small-scale loss of both the UL and the DL is added to the DL
    for i in range(len(Hd)):
        for j in range(len(Hd[i])):
            realpart = Hd[i][j].real
            imagpart = Hd[i][j].imag
            realpart *= np.sqrt(d1[i] ** (-alpha * 2) / pNoise * 10 ** (-2))
            imagpart *= np.sqrt(d1[i] ** (-alpha * 2) / pNoise * 10 ** (-2))
            Hd[i][j] = complex(realpart, imagpart)

    return ChannelModel(Hu, Hd, Hsi)


if __name__ == "__main__":
    import os
    import LogUtil

    os.chdir("D:\wpcn-full-duplex\mat")
    k = 3
    Nt = 4
    alpha = 2
    pNoise = 10 ** (-7)
    times = 2

    import copy

    for _ in xrange(times):
        d = [3 for _ in xrange(k)]
        channel = initChannel(k, Nt, d, alpha, pNoise)

        logger = LogUtil.getLogger(k,Nt,1)
        result = getInitResultModel(channel, True)

        logger.info("Channel : %s" % channel)


        channel2 = copy.deepcopy(channel)
        channel3 = copy.deepcopy(channel)
        channel4 = copy.deepcopy(channel)
        channel5 = copy.deepcopy(channel)
        channel6 = copy.deepcopy(channel)

        result2 = copy.deepcopy(result)
        result3 = copy.deepcopy(result)
        result4 = copy.deepcopy(result)
        result5 = copy.deepcopy(result)
        result6 = copy.deepcopy(result)

        ## fd sum Manager
        Manager = getSumFDManager(channel, result)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result))

        ## fd fair Manager
        Manager = getFairFDManager(channel2, result2)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result2))

        ## hd sum Manager
        Manager = getSumHDManager(channel3, result3)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result3))

        ## hd fair Manager
        Manager = getFairHDManager(channel4, result4)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result4))

        ## fd sum Manger (No noise)
        Manager = getSumFDNosiManager(channel5, result5)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result5))

        ## fd fair Manager (No noise)
        Manager = getFairFDNosiManager(channel6, result6)
        ret = Manager.execute()
        logger.info("flag: %s, result: %s" % (ret, result6))

