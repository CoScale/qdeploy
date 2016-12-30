from subprocess import Popen, PIPE

class Connection:

    def __init__(self, connectionConfig, logging):
        self.logging = logging
        self.host = connectionConfig['host']
        self.user = connectionConfig['user'] or None

    def execute(self, command, shell=False):
        self.logging.warning("@ executing %s" % command)

        p = Popen(command, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.wait()

        self.logging.info("stdout: " + p.stdout.read().rstrip())
        self.logging.info("stderr: " + p.stderr.read().rstrip())
        self.logging.info("exitco: " + str(p.returncode))

    def execute_local(self, command):
        self.execute([command], shell=True)

    def get_host(self):
        if self.user:
            return "%s@%s" % (self.user, self.host)
        else:
            return self.host

    def execute_remote(self, command):


        self.execute(["ssh", self.get_host(), command])

    def test(self):
        self.execute_remote("rsync --version | head -n 1")
