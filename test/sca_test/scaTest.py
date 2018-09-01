from App.InitFactory import *


if __name__ == "__main__":
    import os
    from App import LogUtil

    os.chdir("D:\wpcn-full-duplex\mat")
    channel = initChannel(2,2, [3,4], 2, 10 ** (-7))

    logger = LogUtil.getLogger(2,2,1)
    result = getInitResultModel(channel, False)

    logger.info("Channel : %s" % channel)
    import copy

    channel2 = copy.copy(channel)
    result2 = copy.copy(result)
    Manager = getTestFairFDManager(channel, result)
    ret = Manager.execute()
    logger.info("flag: %s, result: %s" % (ret, result))

    print Manager.itreationResultLists

    Manager2 = getFairFDManager(channel2, result2)
    ret = Manager2.execute()
    logger.info("flag: %s, result: %s" % (ret, result2))

    print Manager2.itreationResultLists
