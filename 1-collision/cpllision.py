#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Date: 2019-07-18 23:08:57

from pwn import *

num = hex(0x21DD09EC-0x02020202*4)
num = int(num,16)

#0x21DD09EC-0x02020202*4=0x19d501e4
s = ssh(user='col',host='pwnable.kr',port=2222,password='guest')

payload = '\x02'*16+p32(num)        #这3个哪个都行,给p32必须传数字，10进制数字或者16进制数字均可，hex(num)是字符串不是数字
#payload = '\x02'*16+'\xe4\x01\xd5\x19'
#payload = '\x03'*16+'\xe0\xfd\xd0\x15'
print len(payload)
p =s.process(argv=['./col',payload])
print p.recv()

