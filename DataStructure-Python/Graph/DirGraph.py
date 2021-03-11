inp = input("Enter : ").split(',')
s = set()
for i in inp:
    a, b = i.split()
    s.add(a)
    s.add(b)
vertices = sorted(list(s))

# adj = [['0'] * len(vertices)] * len(vertices)
adj = [['0' for _ in range(len(vertices))] for _ in range(len(vertices))]
# print(vertices)
# print(adj)
for i in inp:
    a, b = i.split()
    index_a, index_b = -1, -1
    for j in range(len(vertices)):
        if vertices[j] == a:
            index_a = j
    for x in range(len(vertices)):
        if vertices[x] == b:
            index_b = x

    adj[index_a][index_b] = '1'
# print(adj)
print('    '+'  '.join(vertices))
for s in range(len(vertices)):
    print(vertices[s], ':', ', '.join(adj[s]))
