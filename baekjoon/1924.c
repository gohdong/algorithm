#include <stdio.h>
int main(int argc, char const *argv[]) {
  int list[] = {31,28,31,30,31,30,31,31,30,31,30,31};
  int month,date;
  int cal=0;
  scanf("%d %d",&month, &date );
  for(int i=0;i<month-1;i++){
    cal += list[i];
  }
  cal += date;
  if(cal%7 == 1){
    printf("MON\n" );
  }
  else if(cal%7 == 2){
    printf("TUE\n");
  }
  else if(cal%7 == 3){
    printf("WED\n");
  }
  else if(cal%7 == 4){
    printf("THU\n");
  }
  else if(cal%7 == 5){
    printf("FRI\n");
  }
  else if(cal%7 == 6){
    printf("SAT\n");
  }
  else if(cal%7 == 0){
    printf("SUN\n");
  }
}

