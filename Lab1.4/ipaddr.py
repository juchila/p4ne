# отсортировать случайные сети по маске, а затем по ип

import ipaddress
import random


class IPRandomNet(ipaddress.IPv4Network):
    def __init__(self):
        # ipaddress.IPv4Network.__init__(self, net, mask, False)
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)),
                                       strict=False)
        # генерим случайные сети 0x0B000000, 0xDF000000 (от 11.0.0.0 до 24.0.0.0)

    def key_value(self):
        # return self.with_prefixlen
        return int(self.network_address) + (int(self.netmask) << 32)
        # переводим ип в двоичное значение и перемещаем маску вперед на 32 байта (ип и маска состоят из 32 байт каждый)


rnlist = []  # пустой список для объектов типа подсеть
# sp = ""
for i in range(0, 50):
    i += 1
    ipn = IPRandomNet()
    if ipn.is_global:
        rnlist.append(ipn)  # забиваем список объектами типа сеть
        # sp += str(ipn.key_value()) + ','
        # print(ipn.key_value())


def sortfunc(x):
    return x.key_value()


ll = sorted(rnlist, key=sortfunc)
for n in ll: print(n)

# def byMask_key(sp):
#   return sp.split('/')[1]

# print(sorted(sp.split(',')))
