import simpmsg

con = simpmsg.simpserve()
while True:
    inp = input(">>")
    con.sendmsg("jmsg:" + inp + ":test", "192.168.1.2", 3501)
