# Homework #9

## Problem

- [직사각형](https://programmers.co.kr/learn/courses/30/lessons/12900)
- [도둑질](https://programmers.co.kr/learn/courses/30/lessons/42897)

## Solution-1

- [solution-1.py](src/solution-1.py)

```python
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
```

## Solution-2

- [solution-2.py](src/solution-2.py)

```python
def solution(money):
    answer = 0
    length = len(money)

    dp_1 = [0 for _ in range(length+1)]

    for i in range(3, length):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2]+money[i-1])

    dp_2 = [0 for _ in range(length+1)]
    dp_2[2] = money[1]

    for i in range(3, length+1):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2]+money[i-1])

    return max(dp_1[length-1], dp_2[length])
```
