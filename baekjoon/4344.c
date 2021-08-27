#include <stdio.h>

int main() {
    int c;
    double avg;
	int n=0;
    int sum=0;
    int count=0;
    int score_list[1000];
    scanf("%d",&c);
    double avg_list[c];
    for (int i = 0; i < c; i++) {

        scanf("%d",&n);
        sum = 0;
        count= 0;
        for (int j = 0; j < n; j++) {

            scanf("%d",&score_list[j]);
            sum+= score_list[j];
        }

        avg = (double)sum/(double)n;

        for(int j =0; j<n;j++){
        	if((double)score_list[j]>avg){
        		count++;
        	}
        }
        avg_list[i] = (double)count*100 / (double)n;
        

    }
    for(int i=0; i<c; i++){
    	printf("%.3f%%\n",avg_list[i]);
    }

}