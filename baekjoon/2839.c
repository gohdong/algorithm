#include <stdio.h>
int main(int argc, char const *argv[])
{
	int a=0;
	int count=-1;
	scanf("%d",&a);
	if(a%5==0)
	{
		printf("%d\n",a/5);
	}
	else{
		for (int i = a/5; i >= 0  ; i--)
		{
			for(int j=0;j <= a/3;j++){
				if((i*5 + j*3) == a){
					count = i+j;
				}
			}
			if (count != -1)
			{
				break;
			}
		}
		printf("%d\n",count );
	}
}