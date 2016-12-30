
class Logging:

    COLOR_GREEN = "\x1b[6;37;42m"
    COLOR_WHITE = "\x1b[6;30;47m"
    COLOR_BLUE = "\x1b[2;37;44m"
    COLOR_YELLOW = "\x1b[2;37;43m"
    COLOR_RED = "\x1b[2;37;41m"
    COLOR_END = "\x1b[0m"

    def info(self, message):
        print self.COLOR_WHITE + message + self.COLOR_END

    def message(self, message):
        print self.COLOR_BLUE + message + self.COLOR_END

    def warning(self, message):
        print self.COLOR_YELLOW + message + self.COLOR_END

    def error(self, message):
        print self.COLOR_RED + message + self.COLOR_END

