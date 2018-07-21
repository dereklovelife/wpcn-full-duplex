
from model.FdWpcn import SumFdWpcn
import numpy as np
from BaseSCAModel import BaseSCAModel

class TimeAllocationModel(BaseSCAModel):



    def __init__(self, channel, resultModel, client, fdWpcn):
        super(TimeAllocationModel, self).__init__(channel, resultModel, client)
        self.fdWpcn = fdWpcn

    def iteartion(self):
        # pre
        gamma = self.getGamma()

        self.fdWpcn.setGain(gamma)

        # post
        self.resultModel.th = self.fdWpcn.get
        self.resultModel.t = self.fdWpcn.getTime()
        self.resultModel.userOrder = self.fdWpcn.getUserPositionResult()
        self.userOrderChange()

    def getGamma(self):
        St = self.resultModel.sendBeam
        Sr = self.resultModel.recvBeam
        Hu = self.channel.Hu
        Hd = self.channel.Hd

        return self.client.getGamma(self, St, Sr, Hu, Hd)


    def userOrderChange(self):
        Hu = []
        Hd = []

        for i in self.resultModel.userOrder:
            Hu.append(self.channel.Hu[i])
            Hd.append(self.channel.Hd[i])

        self.channel.Hu = Hu
        self.channel.Hd = Hd

