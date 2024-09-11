#include <stdio.h>
int main()
{
  /*
  int integer1, integer2, integer3, sum;
  printf("Please enter the first integer: ");
  scanf("%d", &integer1);
  printf("Please enter the second integer: ");
  scanf("%d", &integer2);
  printf("Please enter the third integer: ");
  scanf("%d", &integer3);
  sum = integer1 + integer2 + integer3;
  printf("Sum is %d. \n", sum);
  */
  int integer;
  int sum = 0;
  printf("Please enter the first integer: ");
  scanf("%d", &integer);
  sum = sum + integer;
  printf("Please enter the second integer: ");
  scanf("%d", &integer);
  sum = sum + integer;
  printf("Please enter the third integer: ");
  scanf("%d", &integer);
  sum = sum + integer;
  printf("Sum is %d. \n", sum);
  return 0;
}