l, s, c = input("Enter Input : ").split(), [], 0
for i in l:
    s.append(i)
    while len(s) > 2 and i == s[-2] and i == s[-3]:
        c, s = c+1, s[:-3] 
print(f'{len(s)}\n'+("Empty" if not s else ''.join(s[::-1]))+('' if c < 2 else '\nCombo : {} ! ! !'.format(c)))