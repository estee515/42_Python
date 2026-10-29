#!/opt/pyenv/shims/python3

import sys


def shrink(str):
    print(str[:8])


def enlarge(str):
    res = str
    while len(res) < 8:
        res += 'Z'
    print(res)


if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) == 8:
            print(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            shrink(arg)