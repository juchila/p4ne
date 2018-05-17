from pysnmp.hlapi import *

ipaddr = "10.31.70.107"
port = 161

transport = ObjectIdentity(ipaddr, port)
communityData = ObjectIdentity('public', mpModel=0)
snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr',0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget((ipaddr, 161)),
                ContextData(),
                ObjectType(snmp_object1))

print((ContextData()))


for i in result:
    for j in i[3]:
        print(j)
#next(result)
result2 = nextCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget((ipaddr, port)),
                  ContextData(),
                  ObjectType(snmp_object2), lexicongraphicMode=False)
#for i in result2:
#    for j in i[3]:
#        print(j)
#next(result2)
# не идти в глубину
