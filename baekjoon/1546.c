#include <stdio.h>

int main( )
{
    int n;
    int score_list[1000];
    double sum=0.0;
    double avg=0;
    int max=0;
    scanf("%d", &n);
    for (int i = 0; i <n ; i++) {
        scanf("%d",&score_list[i]);
        if (score_list[i]>max){
            max = score_list[i];
        }
    }
    for (int j = 0; j < n; j++) {
        sum += ((double)score_list[j]*100)/(double)max;
    }
    avg = sum/n;
    printf("%f",avg);

    return 0;
}

