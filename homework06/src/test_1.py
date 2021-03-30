def solution(arr):
    answer = max(arr)

    while not found:
        for n in arr:
            if answer % n:
                break
        else:
            break

        answer += 1

    return answer
