class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, size, max_collision):
        self.max_collision = max_collision
        self.table = [None]*size
        self.size = size
        self.numberofdata = 0
        self.isPrint = False

    def insert(self, key, value):
        if not self.isPrint:
            sum = 0
            for i in key:
                sum += ord(i)
            hashIndex = sum % self.size
            if self.table[hashIndex] == None:
                self.table[hashIndex] = Data(key, value)
                self.numberofdata += 1
            else:
                collision_checker = 1
                print("collision number {} at {}".format(
                    collision_checker, hashIndex))

                i = 1
                while self.table[(hashIndex + i * i) % self.size] != None:
                    collision_checker += 1
                    print("collision number {} at {}".format(
                        collision_checker, (hashIndex + i * i) % self.size))
                    if collision_checker == self.max_collision:
                        print("Max of collisionChain")
                        break
                    i += 1

                if self.table[(hashIndex + i * i) % self.size] == None:
                    self.table[(hashIndex + i * i) %
                               self.size] = Data(key, value)
                    self.numberofdata += 1

            self.printTable()
            if self.numberofdata == self.size:
                print("This table is full !!!!!!")
                self.isPrint = True

    def printTable(self):
        for i in range(len(self.table)):
            print("#{}      {}".format(i + 1, self.table[i]))
        print("---------------------------")


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
table_size = int(inp[0].split()[0])
max_collision = int(inp[0].split()[1])
data = inp[1].split(',')

Table = hash(table_size, max_collision)
for i in data:
    Table.insert(i.split()[0], i.split()[1])
