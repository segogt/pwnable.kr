#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Date: 2019-07-18 21:11:00

from pwn import *

context.log_level  =  'debug'

p = process(argv=['./0-fd/fd','4660'])
p.sendline('LETMEWIN')
x=p.recv()
while True:
    try:
        print x
        x=p.recv()
    except:
        break
print 'over'