#!/usr/bin/python
# -*- coding: utf-8-*-

from pwn import *
import sys

e = ELF('/bin/ls')
print hex(e.address)  # 文件装载的基地址
#0x400000
print e.symbols
#print hex(e.symbols['write']) # 函数地址
#0x401680
#print hex(e.got['write']) # GOT表的地址
#0x60b070
#print hex(e.plt['write']) # PLT的地址
#0x401680