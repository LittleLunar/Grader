def pantip(k, n, arr, path):

    if n >= len(arr):
        return 0
    if k - arr[n] < 0:
        return pantip(k, n + 1, arr, path)
    else:
        k -= arr[n]
        path.append(arr[n])
        a = pantip(k, n+1, arr, path)
        if k == 0:
            print(' '.join(map(str, path)))
        path.pop()
        b = pantip(k + arr[n], n + 1, arr, path)
        return a + b + 1 if k == 0 else a + b

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(
    arr, inp[0], pattern))
