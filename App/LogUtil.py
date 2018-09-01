

import logging
import os
import time

LOGGER = None

def getLogger(k, nt, pt):

    global LOGGER
    if LOGGER:
        return LOGGER
    LOGGER= logging.getLogger()
    LOGGER.setLevel(logging.INFO)
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    name = "_".join(map(str, ['',k, nt, pt]))
    log_name = log_path + rq + name + '.log'
    logger = logging.FileHandler(log_name, mode="w")
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    logger.setFormatter(formatter)

    LOGGER.addHandler(logger)
    return LOGGER