def odd_list(al):
    templist = al.copy()
    for i in al:
        if i%2==0:
           del templist[templist.index(i)] 
    else : return templist
print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)