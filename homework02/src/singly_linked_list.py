class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True

        return False

    def prepend(self, value):
        if not self.head:
            self.head = Node(value, None)
            return

        self.head = Node(value, self.head)

    def append(self, value):
        if not self.head:
            self.head = Node(value, None)
            return

        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = Node(value, None)

    def set_head(self, index):
        cur_node = self.head

        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        self.head = cur_node

    def access(self, index):
        cur_node = self.head

        if not cur_node:
            return False

        for _ in range(index):
            cur_node = cur_node.next
            if not cur_node:
                return False

        return cur_node.value

    def insert(self, index, value):
        if index < 1:
            self.prepend(value)
            return

        before_node = self.head

        for _ in range(index-1):
            before_node = before_node.next
            if not before_node:
                return False

        tmp_node = Node(value, before_node.next)
        before_node.next = tmp_node

    def remove(self, index):
        if index < 1:
            self.head = self.head.next
            return

        before_node = self.head

        for _ in range(index-1):
            before_node = before_node.next
            if not before_node:
                return False

        before_node.next = before_node.next.next

    def print(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print()


sll = SinglyLinkedList()

print(f'is list empty? {sll.is_empty()}')

sll.prepend(1)      # sll : 1
sll.append(5)       # sll : 1 5
sll.prepend(43)     # sll : 43 1 5
sll.append(2)       # sll : 43 1 5 2
sll.append(3)       # sll : 43 1 5 2 3
sll.prepend(11)     # sll : 11 43 1 5 2 3
sll.insert(3, 10)   # sll : 11 43 1 10 5 2 3
print(f'is list empty? {sll.is_empty()}')


sll.print()
sll.set_head(2)     # sll : 1 10 5 2 3
sll.remove(1)       # sll : 1 5 2 3
sll.print()
print(f'list[1] : {sll.access(1)}')      # sll[1] => 5
sll.print()
