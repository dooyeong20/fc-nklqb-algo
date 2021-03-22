from solution import solution_1, solution_2

# 문제 1 테스트
n_list = [6, 16, 626331]

for n in n_list:
    print(solution_1(n))

# 문제 2 테스트
answer_list = [[1, 2, 3, 4, 3, 4, 9], [1, 3, 2, 4, 2], [5, 5, 5, 5, 2]]
for answers in answer_list:
    print(solution_2(answers))
