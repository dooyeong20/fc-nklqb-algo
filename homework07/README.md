# Homework #7

## Source File

[quick sort](./src/quick_sort.py)

## Source Code

```python
import random


def quicksort(x):
    def recur(start, end):
        if start >= end:
            return

        l, r, mid = start, end, (start + end) // 2
        p = x[mid]

        while l <= r:
            while l <= r and x[l] <= p:
                l += 1

            while l <= r and x[r] >= p:
                r -= 1

            if l < r:
                x[l], x[r] = x[r], x[l]
            else:
                if l <= mid:
                    x[mid], x[l] = x[l], x[mid]
                    mid = l
                else:
                    x[mid], x[r] = x[r], x[mid]
                    mid = r
                break

        recur(start, mid-1)
        recur(mid+1, end)

    recur(0, len(x) - 1)

    return x


a = [random.randint(1, 10) for _ in range(14)]

print('before sort:', a)
print('after sort:', quicksort(a))

```

## Output

```
before sort: [20, 21, 35, 31, 23, 41, 36, 42, 17, 45, 17, 27, 23, 49]
after sort: [17, 17, 20, 21, 23, 23, 27, 31, 35, 36, 41, 42, 45, 49]

before sort: [10, 47, 11, 46, 40, 46, 29, 30, 45, 5, 5, 18, 23, 2]
after sort: [2, 5, 5, 10, 11, 18, 23, 29, 30, 40, 45, 46, 46, 47]
```
