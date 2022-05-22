import os
import sys
home = os.path.expanduser("~")
prodir = os.path.join(home, "joe", "lib")
sys.path.append(prodir)

import jout

def greeting(serverip):
    jout.jout("hello")