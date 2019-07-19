#include <stdio.h>
#include <string.h>
int main(){

    char *p ="\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\xe4\x01\xd5\x19";
    printf("%ld\n",strlen(p));
	int *ip = (int *)p;
	int i;
	int res = 0;
	for (i = 0; i < 5; i++)
	{
        printf("%d-----%x\n",ip[i],ip[i]);
		res += ip[i];
	}
	return res;
    return 0;
}