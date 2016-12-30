
class DeploySimple:
    def __init__(self, connection, taskConfig, logging):
        self.connection = connection
        self.logging = logging
        self.src = taskConfig['src']
        self.dst = taskConfig['dst']

    def run(self):
        self.connection.execute_local("rsync -avhv %s %s:%s --delete" % (
            self.src,
            self.connection.get_host(),
            self.dst
        ))
