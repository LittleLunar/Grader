def three_sum(prim=list):
    if len(prim) >= 3:
        temp = []
        sublist = []
        for i in range(len(prim)):
            for j in range(i+1,len(prim)):
                for k in range(i+j+1,len(prim)):
                    if prim[i] == 0 and prim[j] == 0 and prim[k] == 0 and len(temp) == 0:
                        temp.append([prim[i],prim[j],prim[k]])
                    if prim[i] + prim[j] + prim[k] == 0 and ((prim[i] != 0 and prim[j] != 0 and prim[k] != 0) or len(temp) == 0) :
                        temp.append([prim[i],prim[j],prim[k]])
        else : print(temp)
    else : print("Array Input Length Must More Than 2")

a = [int(x) for x in input("Enter Your List : ").split()]
three_sum(a)