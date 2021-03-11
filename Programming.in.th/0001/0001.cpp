#include <stdio.h>
int main()
{
    unsigned int a, b, c, percent;
    scanf("%d%d%d", &a, &b, &c);
    percent = a + b + c;
    if (percent <= 100 && percent >= 80)
        printf("A");
    else if (percent >= 75)
        printf("B+");
    else if (percent >= 70)
        printf("B");
    else if (percent >= 65)
        printf("C+");
    else if (percent >= 60)
        printf("C");
    else if (percent >= 55)
        printf("D+");
    else if (percent >= 50)
        printf("D");
    else
        printf("F");

    return 0;
}