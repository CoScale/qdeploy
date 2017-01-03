#
# - Command local
#
# Run command on local computer
#
class CommandLocal:

    def __init__(self, connection, config, logging):
        self._command = config["config"]["command"]
        self._connection = connection
        self._logging = logging

    def run(self):
        self._connection.execute_local(self._command)
