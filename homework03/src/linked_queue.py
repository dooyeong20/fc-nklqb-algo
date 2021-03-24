class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if not self.tail:
            self.head = Node(value, None, None)
            self.tail = self.head
            return

        tmp = Node(value, self.tail, None)
        self.tail.next = tmp
        self.tail = tmp

    def get(self):
        if not self.head:
            return None

        val = self.head.value
        self.head = self.head.next

        if not self.head:
            self.tail = None
            return val

        self.head.prev = None

        return val

    def peek(self):
        if not self.head:
            return None

        return self.head.value

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value, end=" ")
            cur_node = cur_node.next
        print()


q = LinkedQueue()

q.put(3)
q.put(2)
q.put(7)
q.put(1)
q.put(10)
q.put(123)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# q.print()
