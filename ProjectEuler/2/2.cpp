#include <stdio.h>
int main()
{
    int a = 1, b = 2, sum = 0, i = 0;
    int tmp;
    while (a <= 4000000 && b <= 4000000)
    {
        printf("i : %d a : %d b : %d sum : %d -> ", i, a, b, sum);
        if (i % 2 == 0)
            sum += b;
        tmp = b;
        b += a;
        a = tmp;
        i += 1;
        printf("i : %d a : %d b : %d sum : %d\n", i, a, b, sum);
    }
    return 0;
}
// NOT DONE YET!!!!