#
# - Command local
#
# Run command on local computer
#
class CommandLocal:

    def __init__(self, connection, config, logging):
        self.command = config["config"]["command"]
        self.connection = connection
        self.logging = logging

    def run(self):
        self.connection.execute_local(self.command)
