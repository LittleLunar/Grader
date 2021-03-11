#include <stdio.h>
int main()
{
    unsigned int n;
    scanf("%d", &n);
    int a[n], min = 2000000000, max = -2000000000;

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        if (a[i] < min)
            min = a[i];
        if (a[i] > max)
            max = a[i];
    }
    printf("%d\n%d", min, max);
    return 0;
}