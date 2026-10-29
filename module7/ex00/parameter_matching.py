#!/opt/pyenv/shims/python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    try:
        parameter = input("What was the parameter? ")
        if parameter == sys.argv[1]:
            print("Good Job!")
        else:
            print("Nope, sorry..")
    except EOFError:
        sys.exit("\nClosing")
    except KeyboardInterrupt:
        sys.exit("\nctrl c")