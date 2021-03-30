def solution(arr):
    answer = max(arr)
    found = False

    while not found:
        for n in arr:
            if answer % n:
                break
        else:
            break

        answer += 1

    return answer
