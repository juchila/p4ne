import glob
import ipaddress
import re


def sss(s):

    m = re.match("^.*? ip address ([0-9\.]+) ([0-9\.]+)$", s)
    if m:
        return {"ip": ipaddress.IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}

   # m = re.match("^interface (.+)", s)
   # if m:
    #    return {"int": m.group(1)}

   # m = re.match("^hostname (.+)", s)
   # if m:
    #    return {"host": m.group(1)}

    return ""


path = "C://Users//av.legkun//Seafile//p4ne_training//config_files//*.txt"
L = glob.glob(path)
# print(len(L))
ipaddr = []
ipint = []
hostname = []

for i in L:
    with open(i) as f:
        # print(f)
        for j in f:
            ss = sss(j)
            if ss != "": ipaddr.append(ss)

print(ipaddr)
