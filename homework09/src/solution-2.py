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
