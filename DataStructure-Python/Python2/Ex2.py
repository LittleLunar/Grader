def odd_even(arr,s):
    li = []
    for i in range(len(arr)):
        if (i+1) % 2 == 0 and s == 'Even':
            li.append(arr[i])
        elif (i+1) % 2 == 1 and s == 'Odd':
            li.append(arr[i])

    if type(arr) == list:
        return print(li)
    elif type(arr) == str:
        return print(''.join(li))

print("*** Odd Even ***")
my_input = [str(x) for x in input("Enter Input : ").split(',',maxsplit=2)]
if my_input[0] == 'L' : 
    odd_even(list(my_input[1].split(' ')),my_input[2])
elif my_input[0] == 'S' :
    odd_even(my_input[1],my_input[2])