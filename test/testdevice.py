import simpmsg

server = simpmsg.simpserve()
server.initserver("0.0.0.0", 3500)

while True:
    com = server.getmsg()[1]
    print(com)