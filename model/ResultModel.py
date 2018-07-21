


## result model
class ResultModel(object):

    def __init__(self):

        # time allocation
        self.t = None

        # throughput
        self.th = None

        # send beamforming
        self.sendBeam = None

        # recv beamforming
        self.recvBeam = None

        # user order
        self.userOrder = None

    def __str__(self):
        strList = []
        strList.append("Time:%s" % (self.t))
        strList.append("Throughput:%s" % (self.th))
        strList.append("SendBeam:%s" % (self.sendBeam))
        strList.append("RecvBeam:%s" % (self.recvBeam))
        strList.append("UserOrder:%s" % (self.userOrder))

        return "\n".join(strList)




