import safepass
import sys
from getpass import getpass


def main():
    if len(sys.argv) > 1:
        if '--version' in sys.argv:
            sys.path.insert(0, '..')
            from setup import VERSION
            print(VERSION)
            result = 0
        else:
            result = True
            for passwd in sys.argv[1:]:
                result = result and safepass.safepass(passwd)
            result = not result
    else:
        passwd = getpass()
        result = not safepass.safepass(passwd)
    sys.exit(result)
