# 문제 1
def solution_1(n):
    ans = 0

    while n != 1:
        n = n // 2 if not n % 2 else n * 3 + 1
        ans += 1

        if ans >= 500:
            return -1

    return ans


# 문제 2
def solution_2(answers):
    answers_len = len(answers)
    ans = [[i, 0] for i in range(1, 4)]

    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(answers_len):
        if pattern_1[i % 5] == answers[i]:
            ans[0][1] += 1

        if pattern_2[i % 8] == answers[i]:
            ans[1][1] += 1

        if pattern_3[i % 10] == answers[i]:
            ans[2][1] += 1

    ans.sort(key=lambda x: -x[1])
    ans = list(filter(lambda x: x[1] == ans[0][1], ans))

    return list(map(lambda x: x[0], ans))
