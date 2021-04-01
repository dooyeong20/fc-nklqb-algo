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


a = [random.randint(1, 10) for _ in range(5)]

print('before sort:', a)
print('after sort:', quicksort(a))
