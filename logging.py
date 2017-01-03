
class Logging:

    _COLOR_GREEN = "\x1b[6;37;42m"
    _COLOR_WHITE = "\x1b[6;30;47m"
    _COLOR_BLUE = "\x1b[2;37;44m"
    _COLOR_YELLOW = "\x1b[2;37;43m"
    _COLOR_RED = "\x1b[2;37;41m"
    _COLOR_END = "\x1b[0m"

    def __init__(self, verbose=False):
        self._verbose = verbose

    def info(self, message):
        if self._verbose:
            print self._COLOR_WHITE + message + self._COLOR_END

    def message(self, message):
        if self._verbose:
            print self._COLOR_BLUE + message + self._COLOR_END

    def warning(self, message):
        print self._COLOR_YELLOW + message + self._COLOR_END

    def error(self, message):
        print self._COLOR_RED + message + self._COLOR_END

