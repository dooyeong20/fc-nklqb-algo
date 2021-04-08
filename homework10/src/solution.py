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

    def _prefix_search(self, word, cnt, totalLength):
        curr = self.root

        for ch in word:
            if ch == '?':
                if totalLength in curr.memo:
                    return curr.memo[totalLength]
                else:
                    return 0

            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return 0

    def search(self, word):
        cnt = 0
        length = len(word)

        if not(word[0] != '?' or (word[0] == '?' and word[-1] == '?')):
            word = word[::-1]
        q_idx = 0

        for i in range(length):
            if word[i] == '?':
                q_idx = i
                break

        cnt = self._prefix_search(word, length - q_idx, length)

        return cnt


def solution(words, queries):
    answer = []
    trie = Trie()
    trieRev = Trie()

    for w in words:
        trie.insert(w)
        trieRev.insert(w[::-1])

    for q in queries:
        if q[0] != '?' or (q[0] == '?' and q[-1] == '?'):
            answer.append(trie.search(q))
        else:
            answer.append(trieRev.search(q))

    return answer
