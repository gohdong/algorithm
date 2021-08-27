#include <stdio.h>

int main(int argc, char const *argv[]) {
  int a;
  scanf("%d",&a);
  for (int i=0 ; i<a;i++){
    for(int k=0; k<i;k++){
      printf(" ");
    }
    for(int j=a; j>i;j--){
      printf("*");
    }
    printf("\n" );
  }

}
