class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break

            if value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'

        # 만약 node가 None 이어도 parent와 direction 모두 다 포함하고 있다.
        return node, parent, direction

    def insert(self, value):
        if self.__search(value)[0]:
            return False

        if not self.root:
            self.root = Node(value, None, None)
            return

        cur = self.root

        while 1:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left = Node(value, None, None)
                    return

            if cur.right:
                cur = cur.right
            else:
                cur.right = Node(value, None, None)
                return

    def search(self, value):
        cur = self.root

        while cur:
            if cur.value == value:
                return True

            cur = cur.left if cur.value > value else cur.right

        return False

    def remove(self, value):
        del_node = self.root
        del_node_parent = None

        while del_node.value != value:
            if del_node.value < value:
                if del_node.right:
                    del_node_parent = del_node
                    del_node = del_node.right
                else:
                    return False
            else:
                if del_node.left:
                    del_node_parent = del_node
                    del_node = del_node.left
                else:
                    return False

        # Case 1 - 자식노드가 없을 때
        if not del_node.left and not del_node.right:
            if del_node.value > del_node_parent.value:  # 오른쪽 자식을 삭제하는 경우
                del_node_parent.right = None
            else:
                del_node_parent.left = None

        # Case 2 - 자식 노드가 좌/우 둘다 있을 때 - 오른쪽 자식 중 가장 작은 값 가져오기
        elif del_node.left and del_node.right:
            repl_node = del_node.right
            repl_parent_node = del_node

            while repl_node.left:
                repl_parent_node = repl_node
                repl_node = repl_node.left

            if repl_parent_node == del_node:
                repl_parent_node.right = repl_node.right
            else:
                repl_parent_node.left = repl_node.right
                repl_node.right = del_node.right

            repl_node.left = del_node.left

            if del_node_parent:
                if del_node.value > del_node_parent.value:
                    del_node_parent.right = repl_node
                else:
                    del_node_parent.left = repl_node
            else:   # 지워지는 노드가 root 노드일 때
                self.root = repl_node

        # Case 3 - 좌/우 중 하나의 자식만 있을 때
        else:
            if del_node.left:
                if del_node.value > del_node_parent.value:
                    del_node_parent.right = del_node.left
                else:
                    del_node_parent.left = del_node.left
            else:
                if del_node.value > del_node_parent.value:
                    del_node_parent.right = del_node.right
                else:
                    del_node_parent.left = del_node.right


bst = BinarySearchTree()

for i in [15, 3, 2, 8, 9, 14, 5, 1, 5, 21, 23, 17, 19]:
    bst.insert(i)

bst.root.display()
bst.remove(15)
bst.remove(3)
bst.remove(5)

print('\n---------------------\n')

bst.root.display()
