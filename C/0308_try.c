#include <stdio.h>
int main()
{

  printf("Hello world!\n");
  printf("Hello \"C\" world!\n");

  int a, b, c;
  printf("please type integer1: \n");
  scanf("%d", &a);
  printf("please type integer2: \n");
  scanf("%d", &b);
  printf("please type integer3: \n");
  scanf("%d", &c);
  printf("a = %d, b= %d, c=%d \n ", a, b, c);
  int temp = c;
  c = b;
  b = a;
  a = temp;
  printf("a = %d, b= %d, c=%d \n ", a, b, c);
  return 0;
}