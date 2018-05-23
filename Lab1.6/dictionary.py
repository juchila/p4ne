import glob
import ipaddress
import re


def sss(s):
    template = ["^.*? ip address ([0-9\.]+) ([0-9\.]+)$", "^interface (.+)", "^hostname (.+)"]
    c = 0
    while c < 3:
        m = re.match(template[c], s)
        if m:
            if c == 0: return [0, {"ip": ipaddress.IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}]
            if c == 1: return [1, {"int": m.group(1)}]
            if c == 2: return [2, {"host": m.group(1)}]
        c += 1
    return ""


L = glob.glob("C://Users//av.legkun//Seafile//p4ne_training//config_files//*.txt")
ipaddr = []
ipint = []
iphost = []
for i in L:
    with open(i) as f:
        for j in f:
            ss = sss(j)
            if ss != "":
                if ss[0] == 0: ipaddr.append(ss[1])
                if ss[0] == 1: ipint.append(ss[1])
                if ss[0] == 2: iphost.append(ss[1])
print(ipaddr)
print(ipint)
print(iphost)
