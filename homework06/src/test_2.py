def solution(phone_book):
    answer = True
    phone_set = set(phone_book)

    for number in phone_set:
        tmp = ''

        for n in number:
            tmp += n
            if tmp != number and tmp in phone_set:
                return False

    return True
