#
# - Deploy clean
#
# Change symlink to next deploy
#
class DeployLive:

    def __init__(self, connection, config, logging):
        self.connection = connection
        self.logging = logging
        self.remote = config['deployment']['remote'].rstrip("/")
        self.release_name = config['deployment']['release_name']

    def run(self):
        # Create symlink from current to current deploy in deploys dir
        self.connection.execute_remote('ln -sfn %s/deploys/%s/ %s/current' % (
            self.remote,
            self.release_name,
            self.remote
        ))