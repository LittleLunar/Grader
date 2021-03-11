def num_grid(lst):

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == '#':
                if i-1 in range(len(lst)) and j-1 in range(len(lst[i-1])):
                    if lst[i-1][j-1] == '-':
                        lst[i-1][j-1] = '1'
                    elif lst[i-1][j-1] != '-' and lst[i-1][j-1] != '#':
                        lst[i-1][j-1] = str(int(lst[i-1][j-1]) + 1)
                if i-1 in range(len(lst)) and j in range(len(lst[i-1])):
                    if lst[i-1][j] == '-':
                        lst[i-1][j] = '1'
                    elif lst[i-1][j] != '-' and lst[i-1][j] != '#':
                        lst[i-1][j] = str(int(lst[i-1][j]) + 1)
                if i-1 in range(len(lst)) and j+1 in range(len(lst[i-1])):
                    if lst[i-1][j+1] == '-':
                        lst[i-1][j+1] = '1'
                    elif lst[i-1][j+1] != '-' and lst[i-1][j+1] != '#':
                        lst[i-1][j+1] = str(int(lst[i-1][j+1]) + 1)
                if i in range(len(lst)) and j-1 in range(len(lst[i-1])):
                    if lst[i][j-1] == '-':
                        lst[i][j-1] = '1'
                    elif lst[i][j-1] != '-' and lst[i][j-1] != '#':
                        lst[i][j-1] = str(int(lst[i][j-1]) + 1)
                if i in range(len(lst)) and j+1 in range(len(lst[i-1])):
                    if lst[i][j+1] == '-':
                        lst[i][j+1] = '1'
                    elif lst[i][j+1] != '-' and lst[i][j+1] != '#':
                        lst[i][j+1] = str(int(lst[i][j+1]) + 1)
                if i+1 in range(len(lst)) and j-1 in range(len(lst[i-1])):
                    if lst[i+1][j-1] == '-':
                        lst[i+1][j-1] = '1'
                    elif lst[i+1][j-1] != '-' and lst[i+1][j-1] != '#':
                        lst[i+1][j-1] = str(int(lst[i+1][j-1]) + 1)
                if i+1 in range(len(lst)) and j in range(len(lst[i-1])):
                    if lst[i+1][j] == '-':
                        lst[i+1][j] = '1'
                    elif lst[i+1][j] != '-' and lst[i+1][j] != '#':
                        lst[i+1][j] = str(int(lst[i+1][j]) + 1)
                if i+1 in range(len(lst)) and j+1 in range(len(lst[i-1])):
                    if lst[i+1][j+1] == '-':
                        lst[i+1][j+1] = '1'
                    elif lst[i+1][j+1] != '-' and lst[i+1][j+1] != '#':
                        lst[i+1][j+1] = str(int(lst[i+1][j+1]) + 1)
            elif lst[i][j] == '-':
                lst[i][j] = '0'
    return lst


print('*** Minesweeper ***')
lst_input = []
input_list = input('Enter input(5x5) : ').split(',')
for e in input_list:
    lst_input.append([i for i in e.split()])
print('\n', *lst_input, sep='\n')
print('\n', *num_grid(lst_input), sep='\n')
