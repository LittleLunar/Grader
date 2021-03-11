print('*** multiplication or sum ***')
inp_list = list(map(int,input('Enter num1 num2 : ').split()))
print('The result is {}'.format(inp_list[0] * inp_list[1] if inp_list[0] * inp_list[1] <= 1000 else inp_list[0] + inp_list[1]))