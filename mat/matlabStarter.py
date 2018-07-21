import matlab.engine



ENGINE = None

def getEngine():
    global ENGINE

    if not ENGINE:
        ENGINE = matlab.engine.start_matlab()

    return ENGINE
