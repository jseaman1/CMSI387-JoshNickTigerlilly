#include <stdio.h>

const char* evenOdd() {
  char even[4] = "EVEN";
  char odd[3] = "ODD";
  int i = -10;
  while (i <= 10) {
    if (i % 2 == 0) {
        printf("%d \t\t %d \t\t EVEN \n" , i, i*i);
    } else {
        printf("%d \t\t %d \t\t ODD \n", i, i*i);
    }
    i++;
  }
}

int main(void) {
  evenOdd();
  return 0;
}
