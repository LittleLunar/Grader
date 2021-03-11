def path(g, fr, p):
    if fr in p[:-1]:
        return True
    if fr not in g.keys():
        return False
    tp = False
    for i in g.get(fr, []):
        if i not in p:
            t = path(g, i, p + [i])
        else:
            tp = True
    return tp or t


g = dict()
inp = input("Enter : ").split(',')
for i in inp:
    a = i.split()
    if a[0] not in g.keys():
        g[a[0]] = []
    g[a[0]].append(a[1])
if not path(g, g[list(g)[0]][0], [g[list(g)[0]][0]]):
    print("Graph has no cycle")
else:
    print("Graph has a cycle")
