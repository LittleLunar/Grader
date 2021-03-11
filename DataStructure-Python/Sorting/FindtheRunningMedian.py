def ascendingQuick(s):
    _ascendingQuick(s, 0, len(s) - 1)


def descendingQuick(s):
    _descendingQuick(s, 0, len(s) - 1)


def _ascendingQuick(s, l, r):
    if r <= l:
        return
    i, j = l, l
    pivot = r
    while j < pivot:
        if s[pivot] >= s[j]:
            s[j], s[i] = s[i], s[j]
            i += 1
        j += 1
    s[pivot], s[i] = s[i], s[pivot]
    pivot, i = i, pivot
    _ascendingQuick(s, l, pivot - 1)
    _ascendingQuick(s, pivot + 1, r)


def _descendingQuick(s, l, r):
    if r <= l:
        return
    i, j = r, r
    pivot = l
    while j > pivot:
        if s[pivot] >= s[j]:
            s[j], s[i] = s[i], s[j]
            i -= 1
        j -= 1
    s[pivot], s[i] = s[i], s[pivot]
    pivot, i = i, pivot
    _descendingQuick(s, l, pivot - 1)
    _descendingQuick(s, pivot + 1, r)


def findMed(s):
    if s[0] == s[-1]:
        return s[0]
    if len(s) == 2:
        return (float(s[0]) + float(s[-1])) / 2.0
    return findMed(s[1:-1])


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l = list(map(int, l))
    t = []
    for i in l:
        t.append(i)
        temp = t.copy()
        ascendingQuick(temp)
        med = findMed(temp)
        print('list = {} : median = {:.1f}'.format(t, med))
