

class ChannelModel(object):

    def __init__(self, Hu, Hd, Hsi):
        self.Hu = Hu
        self.Hd = Hd
        self.Hsi = Hsi

    def __str__(self):
        a = "Hu:%s" % (self.Hu)
        b = "Hd:%s" % (self.Hd)
        c = "Hsi:%s" % (self.Hsi)


        return "\n".join([a,b,c])


