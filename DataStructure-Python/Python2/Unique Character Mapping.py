class Bus:
    def __init__(self,people, fare):
        if people >= 0 and fare >= 0:
            self.people = people
            self.fare = fare
    def __str__(self):
        return 'this bus has {} people with fare = {}'.format(self.people,self.fare)
    def __lt__(self,rhs):
        return self.people*self.fare < \
                 rhs.people*rhs.fare
    def people_in(self,k):
        self.people += k
    def people_out(self,k):
        self.people = 0 if self.people - k < 0 else self.people - k
    def change_fare(self,new_fare):
        self.fare = new_fare
inp = list(map(int,input("Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()))
b1 = Bus(inp[0], inp[2])
b2 = Bus(inp[1], inp[3])
print(b1 if b1 < b2 else b2)
b1.people_in(3)
b1.people_out(6)
b1.change_fare(12)
print(b1)