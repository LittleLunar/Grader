def ThisIsRecursive(lis, end, i=0):
    _ThisIsRecursive(lis, 0, end)


def _ThisIsRecursive(lis, i, end):
    if i >= end:
        return
    if lis[i] > lis[i+1]:
        lis[i], lis[i+1] = lis[i+1], lis[i]
    ThisIsRecursive(i + 1, end)


def bubble(lis):
    _bubble(lis, len(lis))


def _bubble(lis, n):
    ThisIsRecursive(lis, n)
    _bubble(lis, n - 1)


num_list = [int(x) for x in input('Enter Input : ').split()]
bubble(num_list)
print(num_list)
