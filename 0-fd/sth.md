## 1 atoi
atoi将字符串转换为整数，int atoi(const char *nptr) 函数会扫描参数 nptr字符串，会跳过前面的空白字符（例如空格，tab缩进）等
```C
#include <stdlib.h>
#include <stdio.h>
 
int main(void)
{
    int n;
    char *str = "12345.67";
    n = atoi(str);
    printf("n=%d\n",n);
    return 0;
}
//n=12345
```
## 2 int main(int argc, char *argv[], char *envp[])

- argc记录了输入命令从参数的个数，argv保存了参数的内容，argv[0]就是可执行文件的名字，argv[1...n]分别记录了第1...n个参数的内容(字符串)
- char   *envp[]   它是用来取得系统的环境变量的。   
在UNIX或者LINUX下，有系统环境变量，如常用的$PATH,$USER,$HOME等等。   
envp保存所有的环境变量。其格式为（UNIX下）   
PATH=/usr/bin;/local/bin;   
HOME=/home/shuui   
```C
//测试程序
#include <stdio.h>

int main(int argc,char **argv,char *envp[])
{
    int i,x = argc;
    printf("argc : %d\n",x);
    for(i=0;i<x;i++){
        printf("argv[%d] = %s\n",i,argv[i]);
    }
    for(i=0;envp[i]!=NULL;i++){
        printf("envp[%d] = %s\n",i,envp[i]);
    }
    return 0;
}
```
```
➜  0-fd git:(master) ✗ ./test.out aaa bbb ccc ddd

argc : 5
argv[0] = ./test.out
argv[1] = aaa
argv[2] = bbb
argv[3] = ccc
argv[4] = ddd
envp[0] = XDG_SEAT=seat0
envp[1] = XDG_SESSION_ID=2
envp[2] = WINDOWPATH=2
envp[3] = LC_IDENTIFICATION=zh_CN.UTF-8
envp[4] = DISPLAY=:0
envp[5] = COLORTERM=truecolor
envp[6] = JRE_HOME=/opt/jdk1.8.0_201/jre
envp[7] = GNOME_TERMINAL_SERVICE=:1.115
envp[8] = GNOME_DESKTOP_SESSION_ID=this-is-deprecated
envp[9] = DEFAULTS_PATH=/usr/share/gconf/ubuntu.default.path
envp[10] = LOGNAME=segogt
envp[11] = TEXTDOMAIN=im-config
envp[12] = JAVA_HOME=/opt/jdk1.8.0_201
envp[13] = SHELL=/usr/bin/zsh
envp[14] = LC_TIME=zh_CN.UTF-8
envp[15] = PATH=/home/segogt/geth:/opt/jdk1.8.0_201/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
envp[16] = LC_NUMERIC=zh_CN.UTF-8
envp[17] = LC_PAPER=zh_CN.UTF-8
envp[18] = IM_CONFIG_PHASE=2
envp[19] = TEXTDOMAINDIR=/usr/share/locale/
envp[20] = CLUTTER_IM_MODULE=xim
envp[21] = QT4_IM_MODULE=fcitx
envp[22] = XMODIFIERS=@im=fcitx
envp[23] = XDG_MENU_PREFIX=gnome-
envp[24] = GNOME_SHELL_SESSION_MODE=ubuntu
envp[25] = XAUTHORITY=/run/user/1000/gdm/Xauthority
envp[26] = XDG_SESSION_DESKTOP=ubuntu
envp[27] = GDMSESSION=ubuntu
envp[28] = QT_IM_MODULE=fcitx
envp[29] = SSH_AUTH_SOCK=/run/user/1000/keyring/ssh
envp[30] = LC_ADDRESS=zh_CN.UTF-8
envp[31] = LC_MEASUREMENT=zh_CN.UTF-8
envp[32] = XDG_CONFIG_DIRS=/etc/xdg/xdg-ubuntu:/etc/xdg
envp[33] = MANDATORY_PATH=/usr/share/gconf/ubuntu.mandatory.path
envp[34] = CLASSPATH=.:/opt/jdk1.8.0_201/lib:/opt/jdk1.8.0_201/jre/lib:/opt/jdk1.8.0_201/lib/dt.jar:/opt/jdk1.8.0_201/lib/tools.jar
envp[35] = USERNAME=segogt
envp[36] = DESKTOP_SESSION=ubuntu
envp[37] = XDG_RUNTIME_DIR=/run/user/1000
envp[38] = GTK_IM_MODULE=fcitx
envp[39] = USER=segogt
envp[40] = GTK_MODULES=gail:atk-bridge
envp[41] = PWD=/home/segogt/CTF/pwnable/0-fd
envp[42] = VTE_VERSION=5202
envp[43] = LC_MONETARY=zh_CN.UTF-8
envp[44] = HOME=/home/segogt
envp[45] = QT_ACCESSIBILITY=1
envp[46] = DESKTOP_AUTOSTART_ID=10355ecbf85d22a8c1156332749384076300000028510007
envp[47] = SSH_AGENT_PID=2942
envp[48] = XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share:/usr/share:/var/lib/snapd/desktop
envp[49] = LANGUAGE=zh_CN:zh:en_US:en
envp[50] = LANG=zh_CN.UTF-8
envp[51] = LC_NAME=zh_CN.UTF-8
envp[52] = GNOME_TERMINAL_SCREEN=/org/gnome/Terminal/screen/de3d9b21_31d4_4b02_9d17_a1473aafbb31
envp[53] = GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
envp[54] = SHLVL=1
envp[55] = XDG_VTNR=2
envp[56] = XDG_SESSION_TYPE=x11
envp[57] = DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
envp[58] = XDG_CURRENT_DESKTOP=ubuntu:GNOME
envp[59] = TERM=xterm-256color
envp[60] = SESSION_MANAGER=local/segogtPC:@/tmp/.ICE-unix/2851,unix/segogtPC:/tmp/.ICE-unix/2851
envp[61] = LC_TELEPHONE=zh_CN.UTF-8
envp[62] = OLDPWD=/home/segogt/CTF/pwnable
envp[63] = ZSH=/home/segogt/.oh-my-zsh
envp[64] = PAGER=less
envp[65] = LESS=-R
envp[66] = LC_CTYPE=zh_CN.UTF-8
envp[67] = LSCOLORS=Gxfxcxdxbxegedabagacad
envp[68] = LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
envp[69] = _=/home/segogt/CTF/pwnable/0-fd/./test.out
```
## 3 read函数 ssize_t read  (int fd, void *buf, size_t count);
```
函数的返回值说明：
（1）如果成功，返回读取的字节数；

（2）如果出错，返回-1并设置errno；

（3）如果在调read函数之前已是文件末尾，则返回0

函数的参数【int fd】：
这个是文件指针/文件描述符
fd == 0为标准输入 
fd == 1为标准输出 
fd == 2为标准错误输出 

函数的参数【void *buf】：
读上来的数据保存在缓冲区buf中，同时文件的当前读写位置向后移

函数的参数【size_t count】：
是请求读取的字节数。若参数count 为0, 则read()不会有作用并返回0. 返回值为实际读取到的字节数, 如果返回0
```
## 4linux文件描述符
```
fd == 0为标准输入 
fd == 1为标准输出 
fd == 2为标准错误输出 
```
