def mapping(s):
    real_list = []
    temp_list = []
    for i in s:
        for j in temp_list:
            if i == j:
                real_list.append(temp_list.index(j))
                break
        else:
            temp_list.append(i)
            real_list.append(temp_list.index(i))
    else : return real_list
letters = str(input("Enter String : "))
print(mapping(letters))