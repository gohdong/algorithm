#include <stdio.h>
int main(int argc, char const *argv[])
{
	char a[2];
	char k[2];
	a[0]=0;
	a[1]=0;
	int count=0;
	int asd= 14;
	int b,c,d,e;
	scanf("%s",&a);
	if(a[1]==0){
		a[1]=a[0];
		a[0]=48;
	}
	k[0]=a[0];
	k[1]=a[1];
	while(1){
		b = a[0]-48;
		c = a[1]-48;
		d = (b+c)%10;
		a[0]=a[1];
		a[1]=d+48;
		
		count++;
		if(a[0]==k[0] && a[1]==k[1]){
			break;
		}
	}
	printf("%d\n",count );
	return 0;
}