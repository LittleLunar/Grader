class funString:
    def __init__(self,s):
        self.word = s
    def lenString(self):
        return len(self.word)
    def upper_lower_String(self):

        return ''.join([chr(ord(x)-32) if 'a' <= x <= 'z' else chr(ord(x)+32) for x in self.word])
    def reverse_String(self):
        return self.word[::-1]
    def remove_duplicate(self):

        return ''.join(sorted(set(self.word),key=self.word.index))

x,y = input("Enter String and Number of Function : ").split()
a = funString(str(x))
y = int(y)
if y == 1:
    print(a.lenString())
elif y == 2:
    print(a.upper_lower_String())
elif y == 3:
    print(a.reverse_String())
else :
    print(a.remove_duplicate())