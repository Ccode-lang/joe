import os
import sys
home = os.path.expanduser("~")
prodir = os.path.join(home, "joe", "lib")
sys.path.append(prodir)

import jout
import jinput
import simpmsg

internet = simpmsg.simpserve()

def toggle(serverip):
    try:
        jout.jout("what device should I contact")
        device = jinput.jinput()
        internet.sendmsg("jmsg:" + "toggle:" + device, serverip, 3501)
    except:
        jout.jout("sorry something went wrong")
