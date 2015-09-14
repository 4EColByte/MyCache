#!/usr/bin/env python
# coding: utf-8
import pexpect

ipAddress = '202.91.246.186'
loginName = 'bzjs001'
loginPassword = '001bzjs'

cmd = 'ftp ' + ipAddress

child = pexpect.spawn(cmd)
index = child.expect(["(?i)name", "(?i)Unknow host", pexpect.EOF, \
        pexpect.TIMEOUT])
if (index == 0):
    child.sendline(loginName)
    # 期望 "(?i)password" 具有提示输入密码的字符出现.
    index = child.expect(["(?i)password", pexpect.EOF, pexpect.TIMEOUT])
    # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
    if (index != 0):
        print "ftp login failed"
        child.close(force=True)
    # 匹配到了密码提示符，发送密码 + 换行符给子程序.
    child.sendline(loginPassword)
    # 期望登录成功后，提示符 "ftp>" 字符出现.
    index = child.expect(['ftp>', 'Login incorrect', 'Service not available',
    pexpect.EOF, pexpect.TIMEOUT])
    # 匹配到了 'ftp>'，登录成功.
    if (index == 0):
        print 'Congratulations! ftp login correct!'
        # 发送 'bin'+ 换行符给子程序，表示接下来使用二进制模式来传输文件.
        child.sendline("bin")
        print 'getting a file...'
        # 向子程序发送下载文件 rmall 的命令.
        child.sendline("bye")
    # 用户名或密码不对，会先出现 'Login incorrect'，然后仍会出现 'ftp>'，但是 pexpect 是最小匹配，不是贪婪匹配,
    # 所以如果用户名或密码不对，会匹配到 'Login incorrect'，而不是 'ftp>'，然后程序打印提示信息并退出.
    elif (index == 1):
        print "You entered an invalid login name or password. Program quits!"
        child.close(force=True)
    # 匹配到了 'Service not available'，一般表明 421 Service not available, remote server has
    # closed connection，程序打印提示信息并退出.
    # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
    else:
        print "ftp login failed! index = " + index
        child.close(force=True)


# 匹配到了 "(?i)Unknown host"，表示 server 地址不对，程序打印提示信息并退出
elif index == 1:
    print "ftp login failed, due to unknown host"
    child.close(force=True)
# 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出
else:
    print "ftp login failed, due to TIMEOUT or EOF"
    child.close(force=True)
