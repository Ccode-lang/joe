import os
import sys
import argparse
home = os.path.expanduser("~")
prodir = os.path.join(home, "joe", "pro")
sys.path.append(prodir)


import greeting
import jterminate
import jtoggle

prolist = {
    "hello" : greeting.greeting,
    "exit" : jterminate.exit,
    "pass" : jpass,
    "toggle device" : jtoggle.toggle
}
