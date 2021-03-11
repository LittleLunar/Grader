def twobit(x):
    if inp < 0:
        return print('Only Positive & Zero Number ! ! !')
    if inp == 0:
        return print(0)
    if x == inp:
        print(''.join(a))
        return
    a[x] = '0'
    twobit(x + 1)
    a[x] = '1'
    twobit(x + 1)

inp = int(input('Enter Number : '))
a = ['0'] * inp
twobit(0)
