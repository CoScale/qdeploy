#
# - Deploy clean
#
# Change symlink to next deploy
#
class DeployLive:

    def __init__(self, connection, config, logging):
        self._connection = connection
        self._logging = logging
        self._remote = config['deployment']['remote'].rstrip("/")
        self._release_name = config['deployment']['release_name']

    def run(self):
        # Create symlink from current to current deploy in deploys dir
        self._connection.execute_remote('ln -sfn %s/deploys/%s/ %s/current' % (
            self._remote,
            self._release_name,
            self._remote
        ))