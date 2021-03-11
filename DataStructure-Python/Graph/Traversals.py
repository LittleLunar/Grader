def dfs(x):
    if x not in check.keys():
        check[x] = True
        print(x, end=" ")
        for i in d[x]:
            dfs(i)


def bfs(x):
    q = [x]
    while q:
        n = q.pop(0)
        if n not in check2.keys():
            check2[n] = True
            print(n, end=" ")
            for i in d[n]:
                q.append(i)


p = input("Enter : ").split(',')
d = dict()
s = set()
for i in p:
    a, b = i.split()
    if a not in d.keys():
        d[a] = set()
    if b not in d.keys():
        d[b] = set()
    d[a].add(b)
    d[b].add(a)
    s.add(a)
    s.add(b)
check = dict()
check2 = dict()
for i in d:
    d[i] = sorted(list(d[i]))

print("Depth First Traversals : ", end="")
for i in sorted(d.keys()):
    dfs(i)
print("\nBredth First Traversals : ", end="")
for i in sorted(d.keys()):
    bfs(i)
