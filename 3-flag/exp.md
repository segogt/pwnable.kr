## 1
gdb动态调试，发现
```
pwndbg> file flag
Reading symbols from flag...(no debugging symbols found)...done.
pwndbg> b main
Breakpoint 1 at 0x401168
pwndbg> r
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]───────────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x7fffffffdc90 —▸ 0x401ae0 (__libc_csu_fini) ◂— push   rbx
 RBX  0x401ae0 (__libc_csu_fini) ◂— push   rbx
 RCX  0x4
 RDX  0x7fffffffdd68 —▸ 0x7fffffffe13e ◂— 'XDG_SEAT=seat0'
 RDI  0x1
 RSI  0x7fffffffdd58 —▸ 0x7fffffffe119 ◂— '/home/segogt/CTF/pwnable/3-flag/flag'
 R8   0x4
 R9   0xb
 R10  0x16
 R11  0x4100800
 R12  0x401a50 (__libc_csu_init) ◂— push   r14
 R13  0x0
 R14  0x0
 R15  0x0
 RBP  0x7fffffffdc60 ◂— 0x0
 RSP  0x7fffffffdc60 ◂— 0x0
 RIP  0x401168 (main+4) ◂— sub    rsp, 0x10
────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x401168 <main+4>     sub    rsp, 0x10
   0x40116c <main+8>     mov    edi, 0x496658
   0x401171 <main+13>    call   puts <0x402080>
 
   0x401176 <main+18>    mov    edi, 0x64
   0x40117b <main+23>    call   malloc <0x4099d0>
 
   0x401180 <main+28>    mov    qword ptr [rbp - 8], rax
   0x401184 <main+32>    mov    rdx, qword ptr [rip + 0x2c0ee5] <0x6c2070>
   0x40118b <main+39>    mov    rax, qword ptr [rbp - 8]
   0x40118f <main+43>    mov    rsi, rdx
   0x401192 <main+46>    mov    rdi, rax
   0x401195 <main+49>    call   0x400320
─────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rbp rsp  0x7fffffffdc60 ◂— 0x0
01:0008│          0x7fffffffdc68 —▸ 0x401344 (__libc_start_main+404) ◂— mov    edi, eax
02:0010│          0x7fffffffdc70 ◂— 0x0
03:0018│          0x7fffffffdc78 ◂— 0x100000000
04:0020│          0x7fffffffdc80 —▸ 0x7fffffffdd58 —▸ 0x7fffffffe119 ◂— '/home/segogt/CTF/pwnable/3-flag/flag'
05:0028│          0x7fffffffdc88 —▸ 0x401164 (main) ◂— push   rbp
06:0030│ rax      0x7fffffffdc90 —▸ 0x401ae0 (__libc_csu_fini) ◂— push   rbx
07:0038│          0x7fffffffdc98 ◂— 0x0
───────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────────────────────────────────────────────────
 ► f 0           401168 main+4
   f 1           401344 __libc_start_main+404
   f 2           401081 _start+41
```
发现
```
0x401184 <main+32>    mov    rdx, qword ptr [rip + 0x2c0ee5] <0x6c2070>
```
0x6c2070对应的就是flag的值，在这一步给了rdx，于是尝试调试直到这一步
```
───────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS ]───────────────────────────────────────────────────────────────────────────────────────────────────
 RAX  0x6c96b0 ◂— 0x0
 RBX  0x401ae0 (__libc_csu_fini) ◂— push   rbx
 RCX  0x8
 RDX  0x496628 ◂— push   rbp /* 'UPX...? sounds like a delivery service :)' */
 RDI  0x4
 RSI  0x0
 R8   0x1
 R9   0x3
 R10  0x22
 R11  0x0
 R12  0x401a50 (__libc_csu_init) ◂— push   r14
 R13  0x0
 R14  0x0
 R15  0x0
 RBP  0x7fffffffdc60 ◂— 0x0
 RSP  0x7fffffffdc50 —▸ 0x401a50 (__libc_csu_init) ◂— push   r14
 RIP  0x40118b (main+39) ◂— mov    rax, qword ptr [rbp - 8]
────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────────────────────────────────────────────────────────────
   0x401171 <main+13>    call   puts <0x402080>
 
   0x401176 <main+18>    mov    edi, 0x64
   0x40117b <main+23>    call   malloc <0x4099d0>
 
   0x401180 <main+28>    mov    qword ptr [rbp - 8], rax
   0x401184 <main+32>    mov    rdx, qword ptr [rip + 0x2c0ee5] <0x6c2070>
 ► 0x40118b <main+39>    mov    rax, qword ptr [rbp - 8]
   0x40118f <main+43>    mov    rsi, rdx
   0x401192 <main+46>    mov    rdi, rax
   0x401195 <main+49>    call   0x400320
 
   0x40119a <main+54>    mov    eax, 0
   0x40119f <main+59>    leave  
```
可以看到压入rdx的字符串内容就是flag
```
UPX...? sounds like a delivery service :)
```
## 2
```sh
strings flag | grep UPX 
```
直接用strings+grep查找文件就找到了。。。