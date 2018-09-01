from BaseSCAModel import BaseSCAModel

class SendBeamModel(BaseSCAModel):

    def __init__(self, channel, resultModel, client):
        super(SendBeamModel, self).__init__(channel, resultModel, client)

    def iteartion(self):
        # before iteration, properties prepared
        t = self.resultModel.t
        Sr = self.resultModel.recvBeam
        Hu = self.channel.Hu
        Hd = self.channel.Hd
        Hsi = self.channel.Hsi

        # iteration
        St, th = self.client.getSendBeam(t, Sr, Hu, Hd, Hsi)

        # after iteration, result record
        # only update the send beam
        self.resultModel.sendBeam = St
        self.resultModel.th = [x[0] for x in th]

        return self.resultModel.th


