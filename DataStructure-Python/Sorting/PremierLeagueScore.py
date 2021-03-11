def bubble(team, point, gd):
    for i in range(len(point)):
        for j in range(len(point) - 1 - i):
            if point[j] > point[j + 1]:
                point[j], point[j + 1] = point[j + 1], point[j]
                team[j], team[j + 1] = team[j + 1], team[j]
                gd[j], gd[j + 1] = gd[j + 1], gd[j]
            elif point[j] == point[j + 1] and gd[j] > gd[j + 1]:
                team[j], team[j + 1] = team[j + 1], team[j]
                gd[j], gd[j + 1] = gd[j + 1], gd[j]


inp = input('Enter Input : ').split('/')
print('== results ==')
premierLeague = []
for i in inp:
    s = i.split(',')
    t = {}
    t['name'], t['wins'], t['loss'], t['draw'], t['scored'], t['conceded'] = s[0], s[1], s[2], s[3], s[4], s[5]
    premierLeague.append(t)
team = []
point = []
gd = []
for i in premierLeague:
    team.append(str(i.get('name')))
    point.append(int(3 * int(i.get('wins')) + int(i.get('draw'))))
    gd.append(int(i.get('scored')) - int(i.get('conceded')))
bubble(team, point, gd)
conclusion = []
for i in range(len(team)):
    t = []
    t1 = {}
    t1['points'] = point[i]
    t2 = {}
    t2['gd'] = gd[i]
    t.append(team[i])
    t.append(t1)
    t.append(t2)
    conclusion.append(t)
for i in range(len(conclusion) - 1, -1, -1):
    print(conclusion[i])
