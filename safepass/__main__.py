import safepass
import sys
from getpass import getpass


def main():
    if len(sys.argv) > 1:
        passwd = sys.argv[1]
    else:
        passwd = getpass()
    sys.exit(not safepass.safepass(passwd))
