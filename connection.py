from subprocess import Popen, PIPE

class Connection:

    def __init__(self, config, logservice, test = False):
        self._logservice = logservice
        self._host = config['host']
        self._user = config['user'] or None
        self._test = test

    def execute(self, command, shell=False, failOnError=True, safe=False):
        self._logservice.warning("@ executing %s" % command)

        if not self._test or (self._test and safe):
            p = Popen(command, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            p.wait()

            exitcode = p.returncode
            stdout = p.stdout.read().rstrip()
            stderr = p.stderr.read().rstrip()
        else:
            exitcode = -1
            stdout = "command not executed"
            stderr = ""

        self._logservice.info("exitco: " + str(exitcode))
        self._logservice.info("stdout: " + stdout)
        self._logservice.info("stderr: " + stderr)

        if exitcode > 0 and failOnError:
            raise Exception('connection: ssh command failed', command)

        return CommandResult(exitcode, stdout, stderr)

    def execute_local(self, command, safe=False):
        return self.execute([command], shell=True, safe=safe)

    def get_host(self):
        if self._user:
            return "%s@%s" % (self._user, self._host)
        else:
            return self._host

    def execute_remote(self, command, safe=False):
        return self.execute(["ssh", self.get_host(), command], safe=safe)

    def test(self):
        self.execute_remote("rsync --version | head -n 1")

class CommandResult:

    def __init__(self, exitcode, stdout, stdin):
        self.exitcode = exitcode
        self.stdout = stdout
        self.stdin = stdin