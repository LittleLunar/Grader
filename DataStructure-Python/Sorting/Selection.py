def ThisisRecursive(s, end):
    return _ThisisRecursive(s, -999999, 0, 0, end)


def _ThisisRecursive(s, _max, _max_i, i, end):
    if i == end + 1:
        return _max_i
    if _max < s[i]:
        _max = s[i]
        _max_i = i
    return _ThisisRecursive(s, _max, _max_i, i + 1, end)


def selection(s):
    _selection(s, len(s) - 1)


def _selection(s, n):
    if n == 0:
        return
    i = ThisisRecursive(s, n)
    if s[i] != s[n]:
        s[n], s[i] = s[i], s[n]
        print('swap {} <-> {} : {}'.format(s[i], s[n], s))
    _selection(s, n - 1)


s = [int(x) for x in input('Enter Input : ').split()]
selection(s)
print(s)
