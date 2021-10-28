#!/usr/bin/env python3
from scapy.all import *

if __name__ == "__main__":
    IFACES.show()
    rozhranie = IFACES.dev_from_index(1)
    sock = conf.L2socket(iface=rozhranie)

    sock.send("Ahoj", )
