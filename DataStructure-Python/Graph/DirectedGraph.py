def insertion(s):
    for i in range(1,len(s)):
        j = i
        while j > 0 and s[j] < s[j - 1]:
            s[j], s[j - 1] = s[j - 1],s[j]
            j-=1

inp = input("Enter : ").split(',')
graph = {}
node = []
for i in inp:
    t = i.split()
    if t[0] not in node:
        node.append(t[0])
    if t[1] not in node:
        node.append(t[1])
    if t[0] in graph.keys():
        graph[t[0]].append(t[1])
    if t[0] not in graph.keys():
        graph[t[0]] = [t[1]]
insertion(node)
print("  ",end="")
for i in range(len(node)):
    print("  {}".format(node[i]), end="")
print()
for i in range(len(node)):
    temp  = {}
    for j in range(len(node)):
        if node[i] in graph.keys() and node[j] in graph[node[i]]:
            temp[node[j]] = 1
        else:
            temp[node[j]] = 0
    print("{} : {}".format(node[i],temp[node[0]]),end="")
    for j in range(1, len(temp)):
        print(", {}".format(temp[node[j]]),end="")
    print()

    



