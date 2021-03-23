class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def prepend(self, value):
        if not self.head:
            self.head = Node(value, None, None)
            self.tail = self.head
            return

        self.head.prev = Node(value, self.head, None)
        self.head = self.head.prev

    def append(self, value):
        if not self.head:
            self.head = Node(value, None, None)
            self.tail = self.head
            return

        self.tail.next = Node(value, None, self.tail)
        self.tail = self.tail.next

    def set_head(self, index):
        cur_node = self.head

        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        self.head = cur_node
        self.head.prev = None

    def access(self, index):
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        return cur_node.value

    def insert(self, index, value):
        cur_node = self.head

        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        tmp_node = Node(value, cur_node, cur_node.prev)
        tmp_node.prev.next = tmp_node
        tmp_node.next.prev = tmp_node

    def remove(self, index):
        cur_node = self.head

        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print()

    def print_inverse(self):
        cur_node = self.tail
        while cur_node:
            print(cur_node.value, end=' ')
            cur_node = cur_node.prev
        print()


dll = DoublyLinkedList()
print(f'is list empty? {dll.is_empty()}')
dll.append(5)       # list : 5
dll.prepend(11)     # list : 11 5
dll.append(1)       # list : 11 5 1
dll.prepend(2)      # list : 2 11 5 1
dll.append(2)       # list : 2 11 5 1 2
dll.prepend(9)      # list : 9 2 11 5 1 2
dll.print()
print(f'is list empty? {dll.is_empty()}')


# dll.set_head(2)
dll.insert(3, 19)   # list : 9 2 11 19 5 1 2
dll.print()
print(f'list[3] = {dll.access(3)}')
dll.remove(2)       # list : 9 2 19 5 1 2
dll.print()
dll.print_inverse()
