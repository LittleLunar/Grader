def range(a,b=None,c=float(1)):
    if b is None and c == 1:
        mylist = [0.0]
        while mylist[len(mylist) - 1] + c < a:
            mylist.append(mylist[len(mylist) - 1] + c)
        else : return tuple(mylist)
    else :
        if a != int(a) and c == int(c):
            x = len(str(a).split('.')[1])
        elif a == int(a) and c != int(c):
            x = len(str(c).split('.')[1])
        elif a != int(a) and c != int(c):
            x = max(len(str(a).split('.')[1]),len(str(c).split('.')[1]))
        mylist = [float(a)]
        while mylist[len(mylist) - 1] + c < b:
            mylist.append(float(format(float(mylist[len(mylist) - 1] + float(c)),f'.{x}f')))
        else : return tuple(mylist)
print("*** New Range ***")
a = [float(x) for x in input("Enter Input : ").split()]
try :
    print(range(a[0],a[1],a[2]))
except :
    try :
        print(range(a[0],a[1]))
    except :
        print(range(a[0]))