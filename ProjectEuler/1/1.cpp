#include <stdio.h>
int main()
{
    int sum = 0;
    for (int i = 3; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            printf("i : %d sum : %d\n", i, sum);
            sum += i;
        }
    }
    printf("Sum of multiples of 3 or 5 : %d", sum);
    return 0;
}