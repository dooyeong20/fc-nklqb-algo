import sys

sys.setrecursionlimit(1000000)


def solution(n):    # Top Down
    ans = dict()

    def recur(i):
        if i < 3:
            ans[i] = i
            return ans[i]

        if i not in ans:
            ans[i] = (recur(i-1) + recur(i-2)) % 1000000007

        return ans[i]

    return recur(n)
