#
# - Deploy upload
#
# Upload new code and change symlink of next
#

class DeployUpload:

    def __init__(self, connection, config, logging):
        self._connection = connection
        self._logging = logging
        self._release_name = config['deployment']['release_name']
        self._local = config['deployment']['local'].rstrip("/")
        self._remote = config['deployment']['remote'].rstrip("/")

    def run(self):
        # Check if exist previous, next, current, deploys
        # previous, next, current are symlinks
        # deploys contains all the version deployed
        self._connection.execute_remote('mkdir -p %s/deploys/' % self._remote)

        # Create directory for new release
        self._connection.execute_remote('mkdir -p %s/deploys/%s/' % (self._remote, self._release_name))

        # Create symlink from next to current deploy in deploys dir
        self._connection.execute_remote('ln -sfn %s/deploys/%s/ %s/next' % (
            self._remote,
            self._release_name,
            self._remote
        ))

        # Copy files from current to next
        # TODO: Create config and command to copy files from current to next release

        # Resync files from local filesystem to next
        self._connection.execute_local("rsync -avhv %s/ %s:%s/ --delete" % (
           self._local,
           self._connection.get_host(),
           "%s/next" % self._remote
        ))
