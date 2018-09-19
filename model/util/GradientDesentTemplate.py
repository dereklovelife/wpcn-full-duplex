


## gradient iteration template

class GradientDesentTemplate(object):

    def __init__(self):
        self.DEFAULT_ITERATION_TIME = 200
        self.count = 0

    def getGradient(self):
        raise RuntimeError()

    def check(self):
        raise RuntimeError()

    def update(self):
        raise RuntimeError()

    def error(self):
        raise RuntimeError()

    def gradientIteration(self):
        try:
            while self.check() and self.count < self.DEFAULT_ITERATION_TIME:
                self.getGradient()
                self.update()
        except:
            self.error()



