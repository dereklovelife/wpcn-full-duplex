from BaseSCAModel import BaseSCAModel

class TimeAllocationModel(BaseSCAModel):



    def __init__(self, channel, resultModel, client, fdWpcn):
        super(TimeAllocationModel, self).__init__(channel, resultModel, client)
        self.fdWpcn = fdWpcn

    def iteartion(self):
        # get new gamma (after the send/recv beam iteration, gamma needs to be updated.)
        gamma = self.getGamma()
        # set new gamma to the result model, and also start iteration.
        self.fdWpcn.setGain(gamma)

        # use dp to iterate both the time allocation and the user schedule.

        # result record
        self.resultModel.userOrder = self.fdWpcn.getUserPositionResult()
        self.resultModel.th = self.fdWpcn.getTh()
        self.resultModel.t = self.fdWpcn.getTime()
        self.userOrderChange()
        return self.resultModel.th

    def getGamma(self):
        St = self.resultModel.sendBeam
        Sr = self.resultModel.recvBeam
        Hu = self.channel.Hu
        Hd = self.channel.Hd

        return self.client.getGamma(St, Sr, Hu, Hd)


    def userOrderChange(self):
        Hu = []
        Hd = []

        for i in self.resultModel.userOrder:
            Hu.append(self.channel.Hu[i])
            Hd.append(self.channel.Hd[i])

        self.channel.Hu = Hu
        self.channel.Hd = Hd


