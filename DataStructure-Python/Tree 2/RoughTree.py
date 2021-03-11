def re(n):
    if a[n] != -1000000000:
        return
    re(2*n+1)
    re(2*n+2)
    a[n] = min(a[2*n+1], a[2*n+2])
    a[2*n+1] -= a[n]
    a[2*n+2] -= a[n]


inp = input('Enter Input : ').split('/')
a = [-1000000000] * int(inp[0])


if int(inp[0]) // 2 + 1 == len(list(map(int, inp[1].split()))):
    for i in range(len(inp[1].split())):
        a[int(inp[0]) - len(inp[1].split()) + i] = int(inp[1].split()[i])
    re(0)
    print(sum(a))
else:
    print('Incorrect Input')
