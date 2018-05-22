import glob
import os
import ipaddress
import re


path = "C://Users//av.legkun//Seafile//p4ne_training//config_files//"
# L = os.listdir(path)
L = glob.glob(path+"*.txt")
print(len(L))
print(L)
i = 0
# ipnl = []
ipint = []
# ipn = ipaddress.IPv4Interface
substr = "ip address "
while i < len(L):
    with open(L[i]) as f:
        print(f)
        for j in f:
            if re.match("^( )*ip address ([0-9\.]+) ([0-9\.]+)$", j):
                m = re.match("^.*?(([0-9\.]+) ([0-9\.]+))$", j)
                ipint.append(m.group(2))
        i += 1
print(ipint)

