def shortest_path(g, stt, stp, p, d, m):
    if stt == stp and (m == None or d < m[1] or (d == m[1] and len(p) < len(m[0]))):
        m = [p, d]
        return m

    for i in g.get(stt, {}):
        if i not in p:

            tmp = shortest_path(g, i, stp, p + [i], d + g[stt][i], m)

            if tmp:
                m = tmp

    return m


g = dict()
inp = input("Enter : ").split('/')
for i in inp[0].split(','):
    a = i.split()
    if a[0] not in g.keys():
        g[a[0]] = dict()
    g[a[0]][a[2]] = int(a[1])

for i in inp[1].split(','):
    b = i.split()
    path = shortest_path(g, b[0], b[1], [b[0]], 0, None)
    if path:
        print("{} to {} : {}".format(b[0], b[1], "->".join(path[0])))
    else:
        print(f"Not have path : {b[0]} to {b[1]}")
