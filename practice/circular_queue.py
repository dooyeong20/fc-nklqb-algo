import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            print('overflow')
            return False

        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def get(self):
        if self.front == self.rear:
            return None

        val = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        return val

    def peek(self):
        return self.array[self.front]

    def print(self):
        while self.front != self.rear:
            print(self.array[self.front], end=' ')
            self.front = (self.front + 1) % self.capacity
        print()


q = CircularQueue(5)
q.put(6)
q.put(2)
q.put(10)
q.put(6)
q.put(2)
print(q.get())
print(q.get())
q.put(1)
q.put(2)
print(q.get())
print(q.get())
print(q.get())
q.print()
