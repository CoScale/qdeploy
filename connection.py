from subprocess import Popen, PIPE

class Connection:

    def __init__(self, connectionConfig, logging):
        self.logging = logging
        self.host = connectionConfig['host']
        self.user = connectionConfig['user'] or None

    def execute(self, command, shell=False, failOnError=True):
        self.logging.warning("@ executing %s" % command)

        p = Popen(command, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        p.wait()

        exitcode = p.returncode
        stdout = p.stdout.read().rstrip()
        stderr = p.stderr.read().rstrip()

        self.logging.info("exitco: " + str(exitcode))
        self.logging.info("stdout: " + stdout)
        self.logging.info("stderr: " + stderr)

        if exitcode > 0 and failOnError:
            raise Exception('connection: ssh command failed', command)

        return CommandResult(exitcode, stdout, stderr)

    def execute_local(self, command):
        return self.execute([command], shell=True)

    def get_host(self):
        if self.user:
            return "%s@%s" % (self.user, self.host)
        else:
            return self.host

    def execute_remote(self, command):
        return self.execute(["ssh", self.get_host(), command])

    def test(self):
        self.execute_remote("rsync --version | head -n 1")

class CommandResult:

    def __init__(self, exitcode, stdout, stdin):
        self.exitcode = exitcode
        self.stdout = stdout
        self.stdin = stdin