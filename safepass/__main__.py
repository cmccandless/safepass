import safepass
import sys
from getpass import getpass


def is_safe(passwd):
    safe = safepass.safepass(passwd)
    print('SAFE!' if safe else 'NOT SAFE!')
    return safe


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
                result = result and is_safe(passwd)
            result = not result
    else:
        passwd = getpass()
        result = not is_safe(passwd)
    sys.exit(result)
