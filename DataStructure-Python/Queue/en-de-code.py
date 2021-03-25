class Queue:
    def __init__(self, lst = []):
        self.queue = lst
    
    def __str__(self):
        return str(self.queue)

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0

def encode(letter, code):
    for x,y in enumerate(letter):
        if 'a' <= y <= 'z':
            letter[x] = (chr(((ord(y) + int(code.peek()) - 97) % 26) + 97))
            code.enqueue(code.dequeue())
        elif 'A' <= y <= 'Z':
            letter[x] = (chr(((ord(y) + int(code.peek()) - 65) % 26) + 65))
            code.enqueue(code.dequeue())

    print("Encode :",letter)

def decode(letter, code):
    for x,y in enumerate(letter):
        if 'a' <= y <= 'z':
            # print(y,1)
            letter[x] = (chr(ord('z') - ( (ord('z') - ord(y) + int(code.peek())) % 26)))
            code.enqueue(code.dequeue())
        elif 'A' <= y <= 'Z':
            # print(y,2)
            letter[x] = (chr(ord('Z') - ( (ord('Z') - ord(y) + int(code.peek())) % 26)))
            code.enqueue(code.dequeue())
    print("Decode :",letter)


inp = input('Enter String and Code : ').split(',')
inp[0] = inp[0].replace(' ','')
"IlovePython".replace(' ','')
print(inp[0])
letter = list(inp[0])
code = Queue(list(inp[1]))
encode(letter, code)
code = Queue(list(inp[1]))
decode(letter, code)
