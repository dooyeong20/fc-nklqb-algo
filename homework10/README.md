# Homework #10

## Solution

- [solution](src/solution.py)

## Source Code

```python
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.memo = {}

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        curr = self.root
        length = len(word)

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node(ch)

            if length not in curr.memo:
                curr.memo[length] = 1
            else:
                curr.memo[length] += 1

            curr = curr.children[ch]

        curr.data = word


    def search(self, word):
        length = len(word)
        q_idx = 0
        curr = self.root

        for ch in word:
            if ch == '?':
                if length in curr.memo:
                    return curr.memo[length]
                else:
                    return 0

            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return 0


def solution(words, queries):
    answer = []
    trie = Trie()
    trieRev = Trie()

    for w in words:
        trie.insert(w)
        trieRev.insert(w[::-1])

    for q in queries:
        if q[0] != '?':
            answer.append(trie.search(q))
        else:
            answer.append(trieRev.search(q[::-1]))

    return answer
```
