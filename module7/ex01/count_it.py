#!/opt/pyenv/shims/python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    print("parameters: %d" % (len(sys.argv) - 1))
    for arg in sys.argv[1:]:
        print("%s: %d" % (arg, len(arg)))


