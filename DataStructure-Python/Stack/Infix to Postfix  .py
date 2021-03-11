inp = input("Enter Infix : ")
op = []
prio = {'+':1,'-':1,'*':2,'/':2,'^':3}
pos_eq = ''
for i in inp:
    if i not in '+-*/()^':
        pos_eq += i
    elif i == ')':
        while op[-1] != '(':
            pos_eq += op.pop()
        else : op.pop()
    elif i == '(':
        op.append(i)
    else :
        while len(op) > 0 and op[-1] != '(' and prio[i] <= prio[op[-1]]:
            pos_eq += op.pop()
        op.append(i)
else : 
    while len(op) > 0:
        pos_eq += op.pop()
print(f'Postfix : {pos_eq}')