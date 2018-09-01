

class BaseSCAModel(object):

    # channel: channel state
    # resultModel: iteration result record
    # client: matlab client api

    def __init__(self, channel, resultModel, client):
        self.channel = channel
        self.resultModel = resultModel
        self.client = client

    # iteration interface
    def iteartion(self):
        raise Exception("Unsupport.")