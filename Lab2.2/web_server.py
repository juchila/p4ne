# from flask import Flask
import flask
import glob
# import ipaddress
import re
import pprint
import json


app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return str(dir(flask))


@app.route('/configs')
def configs():
    iphost_j = json.dumps(iphost, indent=4)
    return str(iphost_j)


@app.route('/config/<host>')
def config(host):
    if host in iphost:
        return str(ipaddr_struct[host])
    return "not found"


def sss(s):
    template = ["^.*? ip address ([0-9\.]+) ([0-9\.]+)$", "^hostname (.+)"]
    c = 0
    while c < 2:
        m = re.match(template[c], s)
        if m:
            if c == 0:
                return [0, m.group(1) + "/" + m.group(2)]
            if c == 1:
                return [1, m.group(1)]  # hostname обычно перед списком ip адресов
        c += 1
    return ""


L = glob.glob("C://Users//av.legkun//Seafile//p4ne_training//config_files//*.txt")
ipaddr_struct = {}
ipaddr = []
iphost = []
hostname = ""
for i in L:
    with open(i) as f:
        for j in f:
            ss = sss(j)
            if ss != "":
                if ss[0] == 0: ipaddr.append(ss[1])
                if ss[0] == 1:
                    hostname = ss[1]
                    iphost.append(ss[1])
        print(hostname)
        ipaddr_struct[hostname] = ipaddr
        print(len(ipaddr))
        ipaddr = []
pprint.pprint(iphost)
if __name__ == '__main__': app.run(debug=True)
