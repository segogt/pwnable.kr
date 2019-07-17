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