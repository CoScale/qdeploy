#
# - Command remote
#
# Run command on remote computer
#
class CommandRemote:

    def __init__(self, connection, config, logging):
        self.command = config["config"]["command"]
        self.connection = connection
        self.logging = logging

    def run(self):
        self.connection.execute_remote(self.command)
