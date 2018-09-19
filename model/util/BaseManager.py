

class SumHdManager(object):

    def __init__(self,client, channel, resultModel):
        self.client = client
        self.channel = channel
        self.resultModel = resultModel

    def execute(self):
        return self.client.sumth(self.channel.Hu, self.channel.Hd, self.channel.Hsi)



class FairHdManager(object):

    def __init__(self,client, channel, resultModel):
        self.client = client
        self.channel = channel
        self.resultModel = resultModel

    def execute(self):
        return self.client.fairth(self.channel.Hu, self.channel.Hd, self.channel.Hsi)


