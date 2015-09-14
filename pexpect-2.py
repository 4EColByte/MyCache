#!/usr/bin/env phython
# coding: utf-8

import pexpect
import sys


user = 'root'
passwd  = '123456'
#child.logfile = sys.stdout
def ssh_install_keyfile(host, user='root'):
    child = pexpect.spawn('ssh-copy-id -i /root/.ssh/id_rsa.pub %s@%s' % (user, host))
    i = child.expect(['(?i)yes/no?', pexpect.TIMEOUT, pexpect.EOF])
    print child.before
    print i
    if i != 0:
        print 'Failed'
        return
    else:
         child.sendline ('yes')
         print "sendding*****"
    #achild.expect('password: ')
    i = child.expect([pexpect.TIMEOUT, '(?i)password:'])
    print i
    if i != 1:
        print 'Password Failed'
        return
    else:
        print 'password paass'
        child.sendline(passwd)
        'sendding passwold'
        child.close()
if __name__ == "__main__":
    ssh_install_keyfile('192.168.1.208')   
