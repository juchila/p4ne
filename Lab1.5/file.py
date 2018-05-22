import glob
# import ipaddress
import re


path = "C://Users//av.legkun//Seafile//p4ne_training//config_files//"
# L = os.listdir(path)
L = glob.glob(path+"*.txt")
print(len(L))
# print(L)
i = 0
ipnl = []
# ipn = ipaddress.IPv4Interface
substr = "ip address "
while i < len(L):
    # f = open(L[i])
    with open(L[i]) as f:
        print(f)
        for j in f:
            # if j.find(substr) != -1:
            if re.match("^( )*ip address ([0-9\.])+ ([0-9\.])+$", j):
            # if j.lstrip().find(substr) == 0 and j.find("dhcp") == -1:
                print(j) # можно for "ip address" in j:\
                #ipnl.append(j.lstrip().replace(substr, "").replace(" ", "/").replace("\n", ""))
                m = re.match("^[ ]*ip address (([0-9\.]+) ([0-9\.]+))$", j)
                ipnl.append(m.group(2))
                # j.replace(" ", "/")
                # ipnl.append(j)
                # ipn = ipaddress.IPv4Address()
                # if ipn.is_global: print(ipn)
        i += 1
    # f.close()
print(ipnl)

