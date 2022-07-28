import os
import sys
import argparse
home = os.path.expanduser("~")
prodir = os.path.join(home, "joe", "pro")
sys.path.append(prodir)

# You can add custom commands in this config file
# To do so add your module to joe/lib and import it here.
import greeting
import jterminate
import jtoggle
# once you do that ad it to this list. The format is:
# "phrase to activate (all lowercase)" : ModuleName.FunctionToRun
prolist = {
    "hello" : greeting.greeting,
    "exit" : jterminate.exit,
    "pass" : jpass,
    "toggle device" : jtoggle.toggle
}
