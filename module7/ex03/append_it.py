#!/opt/pyenv/shims/python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for string in sys.argv[1:]:
        if string.endswith("ism"):
            continue
        else:
            print(string + "ism")