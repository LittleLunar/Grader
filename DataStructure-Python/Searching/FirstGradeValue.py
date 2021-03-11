def quick(s):
    _quick(s, 0, len(s) - 1)


def _quick(s, l, r):
    if r <= l:
        return
    i, j = l, l
    pivot = r
    while j < pivot:
        if s[pivot] > s[j]:
            s[j], s[i] = s[i], s[j]
            i += 1
        j += 1
    s[pivot], s[i] = s[i], s[pivot]
    pivot, i = i, pivot
    _quick(s, l, pivot - 1)
    _quick(s, pivot + 1, r)


def search(l, r, s, key):
    if r <= l:
        if s[l] > key:
            return s[l]
        return 1000000
    return min(search(l, (l+r) // 2, s, key), search((l+r)//2 + 1, r, s, key))


inp = input("Enter Input : ").split('/')
left = list(map(int, inp[0].split(' ')))
right = list(map(int, inp[1].split(' ')))
quick(left)
for i in right:
    if(search(0, len(left) - 1, left, i) != 1000000):
        print(search(0, len(left) - 1, left, i))
    else:
        print("No First Greater Value")
