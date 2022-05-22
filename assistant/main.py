import os
import sys
import argparse
home = os.path.expanduser("~")
prodir = os.path.join(home, "joe", "pro")
sys.path.append(prodir)
prodir = os.path.join(home, "joe", "lib")
sys.path.append(prodir)

import jinput
import jout

import greeting
import jterminate

serverip = "0.0.0.0"
pronotfound = False

comparser = argparse.ArgumentParser()
comparser.add_argument("-p", "--serverip", required=False, help="The IP address of the home connection server. (If not given it defaults to current machine)")
args = vars(comparser.parse_args())

if not args["serverip"] == None:
    serverip = args["serverip"]

def jpass(server):
    pass

prolist = {
    "hello" : greeting.greeting,
    "exit" : jterminate.exit,
    "pass" : jpass
}

while True:
    inp = jinput.jinput()
    try:
        procall = prolist[inp.lower()]
    except Exception as e:
        jout.jout("I do not understand.")
        procall = prolist["pass"]
    try:
        procall(serverip)
    except NameError:
        pass