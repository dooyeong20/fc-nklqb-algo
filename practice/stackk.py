import array


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)

    def push(self, value):
        if self.top >= self.capacity:
            print('stack overflow')
            return False

        self.array[self.top] = value
        self.top += 1

    def pop(self):
        if self.top < 1:
            print('stack : underflow')
            return None

        self.top -= 1
        return self.array[self.top]

    def peek(self):
        if self.top < 0:
            return None

        return self.array[self.top-1]

    def is_empty(self):
        if self.top < 1:
            return True
        return False

    def print(self):
        for _ in range(self.top):
            print(s.pop(), end=' ')


s = Stack(10)

s.push(1)
s.push(7)
s.push(6)
s.push(27)
s.push(61)
s.push(31)
s.push(19)

s.print()
