#
# - Deploy upload
#
# Upload new code and change symlink of next
#

class DeployUpload:

    def __init__(self, connection, config, logging):
        self.connection = connection
        self.logging = logging
        self.release_name = config['deployment']['release_name']
        self.local = config['deployment']['local'].rstrip("/")
        self.remote = config['deployment']['remote'].rstrip("/")

    def run(self):
        # Check if exist previous, next, current, deploys
        # previous, next, current are symlinks
        # deploys contains all the version deployed
        self.connection.execute_remote('mkdir -p %s/deploys/' % self.remote)

        # Create directory for new release
        self.connection.execute_remote('mkdir -p %s/deploys/%s/' % (self.remote, self.release_name))

        # Create symlink from next to current deploy in deploys dir
        self.connection.execute_remote('ln -sfn %s/deploys/%s/ %s/next' % (
            self.remote,
            self.release_name,
            self.remote
        ))

        # Copy files from current to next
        # TODO: Create config and command to copy files from current to next release

        # Resync files from local filesystem to next
        self.connection.execute_local("rsync -avhv %s/ %s:%s/ --delete" % (
           self.local,
           self.connection.get_host(),
           "%s/next" % self.remote
        ))
