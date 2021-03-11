def mondstadt(n):
    if n >= len(power):
        return 0
    l = mondstadt(2*n + 1)
    r = mondstadt(2*n + 2)
    powerOfGroup[n] += (l + r)
    return powerOfGroup[n]


power = []
inp = input('Enter Input : ').split('/')
for i in inp[0].split():
    power.append(int(i))
powerOfGroup = power.copy()
mondstadt(0)
print(powerOfGroup[0])
for i in inp[1].split(','):
    if powerOfGroup[int(i.split()[0])] < powerOfGroup[int(i.split()[1])]:
        print('{}<{}'.format(i.split()[0], i.split()[1]))
    elif powerOfGroup[int(i.split()[0])] > powerOfGroup[int(i.split()[1])]:
        print('{}>{}'.format(i.split()[0], i.split()[1]))
    if powerOfGroup[int(i.split()[0])] == powerOfGroup[int(i.split()[1])]:
        print('{}={}'.format(i.split()[0], i.split()[1]))
