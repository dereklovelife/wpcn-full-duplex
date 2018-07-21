

from BaseSCAModel import  BaseSCAModel

class RecvBeamModel(BaseSCAModel):

    def __init__(self, channel, resultModel, client):
        super(RecvBeamModel, self).__init__(channel, resultModel, client)

    def iteartion(self):
        # pre
        t = self.resultModel.t
        St = self.resultModel.SendBeam
        Hu = self.channel.Hu
        Hd = self.channel.Hd
        Hsi = self.channel.Hsi

        Sr, th = self.client.getRecvBeam(t, St, Hu, Hd, Hsi)

        # post
        self.resultModel.sendBeam = Sr
        self.resultModel.th = th

        return th
