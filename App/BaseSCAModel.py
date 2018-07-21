

class BaseSCAModel(object):

    def __init__(self, channel, resultModel, client):
        self.channel = channel
        self.resultModel = resultModel
        self.client = client

    def iteartion(self):
        raise Exception("Unsupport.")