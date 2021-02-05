#include <stdio.h>

int main(int arc, char *argv[]){
    
  char name[32], age[32], year[32], sign[32], netWorth[32], religion[32];
  
  printf("Please enter your info (32 char limit per item)\n");
  printf("Enter your name: ");
  scanf("%s", &name);
  printf("Enter your age: ");
  scanf("%s", &age);
  printf("Enter your class year: ");
  scanf("%s", &year);
  printf("Enter your astrological sign: ");
  scanf("%s", &sign);
  printf("Enter your net worth: ");
  scanf("%s", &netWorth);
  printf("Enter your religious affiliation: ");
  scanf("%s", &religion);
    
  printf("\nOUTPUT\n---------------------------\n name: %s\nage: %s\n class year: %s\n sign: %s\n net worth: %s\n religion: %s\n", name, age, year, sign, netWorth, religion);

  return 0;
}
