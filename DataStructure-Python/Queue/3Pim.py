class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = list(li)

    def enQueue(self, i):
        self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def getItemCopy(self):
        return self.queue.copy()


def encodemsg(queue, series):
    temp_q, temp_s = ''.join(queue.getItemCopy()).replace(
        ' ', ''), ''.join(series.getItemCopy())

    new_list = []

    in_q = in_s = 0

    while in_q < len(temp_q):
        if ord('A') <= ord(temp_q[in_q]) + int(temp_s[in_s]) <= ord('Z') or ord('a') <= ord(temp_q[in_q]) + int(temp_s[in_s]) <= ord('z'):
            new_list.append(chr(ord(temp_q[in_q]) + int(temp_s[in_s])))

        elif ord(temp_q[in_q]) + int(temp_s[in_s]) > ord('z'):
            new_list.append(
                chr(ord('a') - 1 + (int(temp_s[in_s]) - ord('z') + ord(temp_q[in_q]))))

        elif ord(temp_q[in_q]) + int(temp_s[in_s]) > ord('Z'):
            new_list.append(
                chr(ord('A') - 1 + (int(temp_s[in_s]) - ord('Z') + ord(temp_q[in_q]))))

        in_q += 1
        in_s += 1
        if in_s == temp_s.size():
            in_s = 0

    print('Encode message is : {}'.format(new_list))


def decodemsg(queue, series):
    print('Decode message is : {}'.format(list(
        ''.join(queue.getItemCopy()).replace(' ', ''))))


string, number = input("Enter String and Code : ").split(',')

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)
