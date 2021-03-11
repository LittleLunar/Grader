def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if(x % i == 0):
                return False
        return True
    return False


def findPrimeNum(x):
    j = x
    while True:
        if(isPrime(j)):
            return j
        j += 1


def ReSizeTable():
    global maxCollision
    global Table
    global Threshold
    global percentThres
    global data_count
    global allData
    newSize = findPrimeNum(len(Table) * 2)
    tmp = []
    for i in range(len(Table)):
        if Table[i] != None:
            tmp.append(Table[i])
    Table = [None] * newSize
    data_count = 0
    Threshold = int(newSize * percentThres / 100)
    for i in range(len(tmp)):
        if data_count + 1 > Threshold:
            print("****** Data over threshold - Rehash !!! ******")
            ReSizeTable()

        n = allData[i] % len(Table)
        while Table[n] != None:
            count_collision = 1
            print("collision number {} at {}".format(count_collision, n))
            j = 1
            while Table[(n + j*j) % len(Table)] != None:
                count_collision += 1
                print("collision number {} at {}".format(
                    count_collision, (n + j*j) % len(Table)))
                if(count_collision == maxCollision):
                    break
                j += 1

            if(count_collision == maxCollision):
                print("****** Max collision - Rehash !!! ******")
                ReSizeTable()
                n = allData[i] % len(Table)
                continue
            n = (n + j*j) % len(Table)

        if Table[n] == None:
            Table[n] = allData[i]
            data_count += 1


def printTable():
    global Table
    for i in range(len(Table)):
        print("#{}\t{}".format(i+1, Table[i]))
    print("----------------------------------------")


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
Table = [None] * int(inp[0].split()[0])
maxCollision = int(inp[0].split()[1])
percentThres = int(inp[0].split()[2])
Threshold = int(len(Table) * percentThres / 100)
data_count = 0
allData = list(map(int, inp[1].split()))
print("Initial Table :")
printTable()
for i in range(len(allData)):
    print(f"Add : {allData[i]}")
    if data_count + 1 > Threshold:
        print("****** Data over threshold - Rehash !!! ******")
        ReSizeTable()
    n = allData[i] % len(Table)
    while Table[n] != None:
        count_collision = 1
        print("collision number {} at {}".format(count_collision, n))
        j = 1
        while Table[(n + j*j) % len(Table)] != None:
            count_collision += 1
            print("collision number {} at {}".format(
                count_collision, (n + j*j) % len(Table)))
            if(count_collision == maxCollision):
                break
            j += 1

        if(count_collision == maxCollision):
            print("****** Max collision - Rehash !!! ******")
            ReSizeTable()
            n = allData[i] % len(Table)
            continue

        n = (n + j*j) % len(Table)

    if Table[n] == None:
        Table[n] = allData[i]
        data_count += 1
    printTable()
