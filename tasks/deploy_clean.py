#
# - Deploy clean
#
# Clean up old deploys and other deploy files
#
class DeployClean:

    def __init__(self, connection, config, logging):
        self._connection = connection
        self._logging = logging
        self._remote = config['deployment']['remote'].rstrip("/")
        self._history = 10

    def run(self):
        # Get list of builds
        result = self._connection.execute_remote('ls -1a %s/deploys/' % self._remote, safe=True)
        builds = []
        for line in result.output.splitlines():
            if line != "." and line != "..":
                builds.append(line)

        builds.sort(reverse=True)
        print "Number of builds %s/%s" % (len(builds), self._history)
        if len(builds) > self._history:
            while(len(builds) > self._history):
                buildname = builds.pop()
                print "Removing build %s" % buildname
                self._connection.execute_remote('rm -rfv %s/deploys/%s/' % (self._remote, buildname))
