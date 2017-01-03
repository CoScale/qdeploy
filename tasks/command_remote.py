#
# - Command remote
#
# Run command on remote computer
#
class CommandRemote:

    def __init__(self, connection, config, logging):
        self._command = config["config"]["command"]
        self._connection = connection
        self._logging = logging

    def run(self):
        self._connection.execute_remote(self._command)
