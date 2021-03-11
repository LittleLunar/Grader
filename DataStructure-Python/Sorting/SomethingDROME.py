def ascendingBubble(s):
    for i in range(len(s)):
        for j in range(len(s) - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]


def descendingBubble(s):
    for i in range(len(s)):
        for j in range(len(s) - 1 - i):
            if s[j] < s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]


s = []
for i in input('Enter Input : '):
    s.append(int(i))
a = s.copy()
d = s.copy()
ascendingBubble(a)
descendingBubble(d)
if len(set(s)) == 1:
    print('Repdrome')
elif s == a and len(s) == len(set(s)):
    print('Metadrome')
elif s == a and len(s) != len(set(s)):
    print('Plaindrome')
elif s == d and len(s) == len(set(s)):
    print('Katadrome')
elif s == d and len(s) != len(set(s)):
    print('Nialpdrome')
else:
    print('Nondrome')
