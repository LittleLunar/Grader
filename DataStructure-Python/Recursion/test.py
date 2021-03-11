def print1ToN(n):
    if n <= 1:
        print(1, end=" ")
        return
    print1ToN(n - 1)
    print(n, end=" ")


def printNTo1(n):
    if n <= 1:
        print(1, end=" ")
        return
    print(n, end=" ")
    printNTo1(n - 1)

def twobit(x):
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
        return
    if n == 0:
        print(0)
        return
    if x == n:
        print("".join(a))
        return
    a[x] = '0'
    twobit(x + 1)
    a[x] = '1'
    twobit(x + 1)

def length(s):
    if s[0] is s[-1]:
        print(s[0],end="*")
        return 1
    ns = length(s[:-1])
    print(s[ns], end="*" if s % 2 == 0 else "~")
    return ns + 1
    
n = int(input("Enter Input : "))
a = ['0'] * n
twobit(0)

