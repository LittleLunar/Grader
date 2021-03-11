n = input("Enter Input : ").split(',')
temp = []
for i in range(len(n)):
    while len(temp) > 0 and int(temp[-1].split(' ')[0]) < int(n[i].split(' ')[0]):
        print(temp[-1].split(' ')[1])
        temp.pop()
    else:
        temp.append(n[i])