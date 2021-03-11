print('*** Converting hh.mm.ss to seconds ***')
times = list(map(int,input('Enter hh mm ss : ').split()))
if times[1] > 59 or times[1] < 0:
    print(f'mm({times[1]}) is invalid!')
elif times[2] > 59 or times[2] < 0:
    print(f'ss({times[2]}) is invalid!')
else:
    print('{}:{}:{} = {} seconds'.format('0' + str(times[0]) if len(str(times[0])) < 2 else str(times[0]),'0' + str(times[1]) if len(str(times[1])) < 2 else str(times[1]),'0' + str(times[2]) if len(str(times[2])) < 2 else str(times[2]),'{:,}'.format(times[0] * 3600 + times[1] * 60 + times[2])))