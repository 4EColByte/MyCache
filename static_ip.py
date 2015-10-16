#!/usr/bin/env python
# coding=utf-8
# 设置静态ip脚本
# 使用示例:python static_ip.py -i 10.200.103.107 -n 255.255.252.0  -g 10.200.100.1 -d1 8.8.8.8  -d2 114.114.114.114


import argparse
from os import system


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str)
    parser.add_argument('-n', type=str)
    parser.add_argument('-g', type=str)
    parser.add_argument('-d1', type=str)
    parser.add_argument('-d2', type=str)
    args = parser.parse_args()
    return vars(args)


fn = '/root/gitrepo/MyCache/ifcfg-eth1'


#with open(fn, "r") as f1:
#    k = f1.readlines()
#    for x in k:
#        if "IPADDR" in x:
#            IPADDR = x
#        elif "NETMASK" in x:
#            NETMASK = x
#        elif "GATEWAY" in x:
#            GATEWAY = x
#        elif "DNS1" in x:
#            DNS1 = x
#        elif "DNS2" in x:
#            DNS2 = x
#    print IPADDR,NETMASK
#    f1.close()
settins = ['IPADDR','NETMASK','GATEWAY','DNS1','DNS2']
#def reps()


def staticnetwork():
    args = getargs()
    ip = args['i']
    netmask = args['n']
    gateway = args['g']
    dns1 = args['d1']
    dns2 = args['d2']
    #print ip,netmask,gateway,dns1,dns2
    _content = []
    with open(fn, "r+") as f:
         for line in f:
             _content.append(line)
         #print _content
         for items in _content:
             if items.find('IPADDR') > -1 :
                 items = 'IPADDR=%s\n' % ip
                 print items
             if items.find('NETMASK') > -1 :
                 items = 'NETMASK=%s\n' % netmask
             if items.find('GATEWAY') > -1 :
                 items = 'GATEWAY=%s\n' % gateway
             if items.find('DNS1') > -1 :
                 items = 'DNS1=%s\n' % dns1
             if items.find('DNS2') > -1 :
                 items = 'DNS2=%s\n' % dns2
    with open(fn, 'w') as fn1:
         for items in _content:
             fn1.write(itmes)
    #    d = d.replace(IPADDR, "IPADDR=%s\n" % ip)
    #    d = d.replace(NETMASK, "NETMASK=%s\n" % netmask)
    #    d = d.replace(GATEWAY, "GATEWAY=%s\n" % gateway)
    #    d = d.replace(DNS1, "DNS1=%s\n" % dns1)
    #    d = d.replace(DNS2, "DNS2=%s\n" % dns2)
    #    f.truncate(0)
    #    f.seek(0)
    #    f.write(d)


if __name__ == "__main__":
    staticnetwork()
    #system('ifdown eth0 && ifup eth0')
