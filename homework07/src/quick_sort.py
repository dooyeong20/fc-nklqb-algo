import random


def quicksort(x):
    def sort(left_idx, right_idx):
        if left_idx >= right_idx or right_idx < 0:
            return

        left, right = left_idx, right_idx
        pivot = (left_idx + right_idx) // 2
        pivot_val = x[pivot]

        while 1:
            while left_idx <= right_idx and x[left_idx] <= pivot_val:
                left_idx += 1

            while left_idx <= right_idx and x[right_idx] >= pivot_val:
                right_idx -= 1

            if left_idx <= right_idx:
                x[left_idx], x[right_idx] = x[right_idx], x[left_idx]
            else:
                if left_idx <= pivot:
                    x[pivot], x[left_idx] = x[left_idx], x[pivot]
                    pivot = left_idx
                else:
                    x[pivot], x[right_idx] = x[right_idx], x[pivot]
                    pivot = right_idx
                break

        sort(left, pivot - 1)
        sort(pivot + 1, right)

    sort(0, len(x) - 1)

    return x


a = [random.randint(1, 50) for _ in range(14)]

print('before sort:', a)
print('after sort:', quicksort(a))
