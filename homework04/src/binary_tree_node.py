from collections import deque


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node):
            if node is None:
                return

            print(node.value, end=' ')
            recursive(node.left)
            recursive(node.right)

        recursive(self.root)

    def inorder(self):
        def recursive(node):
            if node is None:
                return

            recursive(node.left)
            print(node.value, end=' ')
            recursive(node.right)

        recursive(self.root)

    def postorder(self):
        def recursive(node):
            if node is None:
                return

            recursive(node.left)
            recursive(node.right)
            print(node.value, end=' ')

        recursive(self.root)

    def bfs(self, value):
        q = deque([self.root])

        while q:
            cur = q.popleft()

            if cur.value == value:
                return True

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

        return False

    def dfs(self, value):
        isFound = False

        def recursive(node):
            nonlocal isFound

            if node.value == value:
                isFound = True
                return

            if isFound is True:
                return

            if node.left is not None:
                recursive(node.left)

            if node.right is not None:
                recursive(node.right)

        recursive(self.root)

        return isFound


li = [i for i in range(1, 10)]
bt = BinaryTree(li)

print('pre ', end=' ')
bt.preorder()           # pre  1 2 4 8 9 5 3 6 7
print()

print('in ', end=' ')
bt.inorder()            # in  8 4 9 2 5 1 6 3 7
print()

print('post ', end=' ')
bt.postorder()          # post  8 9 4 5 2 6 7 3 1
print()

print('bfs ', end=' ')
print(bt.bfs(5))        # bfs  True

print('dfs ', end=' ')
print(bt.dfs(1))        # dfs  True
