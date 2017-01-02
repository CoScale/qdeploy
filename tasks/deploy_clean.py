#
# - Deploy clean
#
# Clean up old deploys and other deploy files
#
class DeployClean:

    def __init__(self, connection, config, logging):
        self.connection = connection
        self.logging = logging
        self.remote = config['deployment']['remote'].rstrip("/")
        self.history = 10

    def run(self):
        # Get list of builds
        result = self.connection.execute_remote('ls -1a %s/deploys/' % self.remote)
        builds = []
        for line in result.stdout.splitlines():
            if line != "." and line != "..":
                builds.append(line)

        builds.sort(reverse=True)
        print "Number of builds %s/%s" % (len(builds), self.history)
        if len(builds) > self.history:
            while(len(builds) > self.history):
                buildname = builds.pop()
                print "Removing build %s" % buildname
                self.connection.execute_remote('rm -rfv %s/deploys/%s/' % (self.remote, buildname))