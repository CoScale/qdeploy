import subprocess
import sys

class Connection:

    def __init__(self, config, logservice, test = False):
        self._logservice = logservice
        self._host = config['host']
        self._user = config['user'] or None
        self._test = test

    def execute(self, command, shell=False, failOnError=True, safe=False):
        self._logservice.warning("@ executing %s" % command)

        if not self._test or (self._test and safe):
            p = subprocess.Popen(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = ""
            while True:
                nextline = p.stdout.readline()
                if nextline == '' and p.poll() is not None:
                    break
                output += nextline
                sys.stdout.write(nextline)
                sys.stdout.flush()

            p.wait()

            exitcode = p.returncode
        else:
            exitcode = -1
            print "command not executed"

        self._logservice.info("exitcode: " + str(exitcode))

        if exitcode > 0 and failOnError:
            raise Exception('connection: ssh command failed', command)

        return CommandResult(exitcode, output)

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

    def __init__(self, exitcode, output):
        self.exitcode = exitcode
        self.output = output
