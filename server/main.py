import os
import simpmsg
import json

class InputError(Exception):
    pass

with open("config.json") as configdata:
    config = json.load(configdata)
    devicelist = config['connections']
    verbose = config["settings"]["verbose"]
if verbose:
    print("Loading server")
server = simpmsg.simpserve()
server.initserver("0.0.0.0", 3501)
if verbose:
    print("Server loaded, waiting for message.")
while True:
    com = server.getmsg()
    if verbose:
        print("Got message \"" + com[1] + "\" from " + com[0])
    if com[1].startswith("jmsg:"):
        args = com[1].split(":")
        try:
            if len(args) == 3:
                try:
                    device = devicelist[args[2]]
                except:
                    raise InputError("Device that client tried to contact does not exist.")
                try:
                    if verbose:
                        print("sending message \"" + args[1] + "\" to device " + args[2])
                    server.sendmsg("jcom:" + args[1], device, 3500)
                except Exception as e:
                    print(repr(e))
            else:
                raise InputError("Too many arguments from client.")
        except InputError as e:
            if verbose:
                print(repr(e))
    else:
        if verbose:
            print("Invalid message from client.")
