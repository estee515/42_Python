#!/opt/pyenv/shims/python3

import sys

if len(sys.argv) <2:
    print("none")
else:
    z_ret = []
    for char in sys.argv[1]:
        if char == 'z':
            z_ret.append('z')
    if len(z_ret) == 0:
        print("none")
    else:
        print(''.join(z_ret))