def bi_search(l, r, arr, x):
    if r <= l:
        if arr[l] == x:
            return True
        return False
    return bi_search(l, (l+r)//2, arr, x) or bi_search((l + r) // 2 + 1, r, arr, x)


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
