def ThisisRecursive(lis, i):
    if i == 0 or lis[i] >= lis[i-1]:
        return
    if lis[i] < lis[i-1]:
        lis[i], lis[i-1] = lis[i-1], lis[i]
    ThisisRecursive(lis, i - 1)


def insertion(lis):
    _insertion(lis, 0, len(lis))


def _insertion(lis, i, n):
    if i == n:
        return
    ThisisRecursive(lis, i)
    _insertion(lis, i + 1, n)


s = [5, 2, 4, 8, 9, 3, 1, 7, 6, 0]
insertion(s)
print(s)
