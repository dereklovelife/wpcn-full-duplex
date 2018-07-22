


class Executor(object):

    def __init__(self, SCAManager, ):
        self.manager = SCAManager

    def run(self):
        return self.manager.execute()

