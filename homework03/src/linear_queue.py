import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear >= self.capacity:
            print("overflow")
            return False

        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        if self.front == self.rear:
            print("empty queue")
            return False

        val = self.array[self.front]
        self.front += 1

        return val

    def peek(self):
        if self.front == self.rear:
            return None

        return self.array[self.front]

    def print(self):
        while self.front < self.rear:
            print(self.array[self.front], end=' ')
            self.front += 1
        print()


q = LinearQueue(5)
print(q.peek())

q.put(4)
q.put(1)
q.put(9)
q.put(12)
q.put(3)
q.put(23)   # overflow

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.put(25)   # overflow

q.print()
