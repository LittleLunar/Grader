def bi_search(a, l, r, x):
    if r <= l:
        if a[l] == x:
            return True
        return False
    return bi_search(a, l, (l+r)//2, x) or bi_search(a, (l+r) // 2 + 1, r, x)


inp = input("Enter Input : ").split('/')
a, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(sorted(a), 0, len(a) - 1, k))