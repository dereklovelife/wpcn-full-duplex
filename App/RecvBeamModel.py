

from BaseSCAModel import  BaseSCAModel

class RecvBeamModel(BaseSCAModel):

    def __init__(self, channel, resultModel, client):
        super(RecvBeamModel, self).__init__(channel, resultModel, client)

    def iteartion(self):
        # pre
        t = self.resultModel.t
        St = self.resultModel.sendBeam
        Hu = self.channel.Hu
        Hd = self.channel.Hd
        Hsi = self.channel.Hsi

        Sr, th = self.client.getRecvBeam(t, St, Hu, Hd, Hsi)

        # post
        self.resultModel.recvBeam = Sr
        self.resultModel.th = [x[0] for x in th]

        return self.resultModel.th
