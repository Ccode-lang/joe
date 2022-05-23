import os
import simpmsg

class InputError(Exception):
    pass

devicelist = {
    "test" : "0.0.0.0"
}

server = simpmsg.simpserve()
server.initserver("0.0.0.0", 3501)
while True:
    com = server.getmsg()[1]
    if com.startswith("jmsg:"):
        args = com.split(":")
        try:
            if len(args) == 3:
                try:
                    device = devicelist[args[2]]
                except:
                    raise InputError("Device does not exist.")
                server.sendmsg(args[1], device, 3500)
            else:
                raise InputError("Too many arguments.")
        except InputError as e:
            print(repr(e))
            pass
    else:
        print("Invalid message.")
        pass
