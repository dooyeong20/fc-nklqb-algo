def solution(distance, rocks, n):
    def get_count(dis):
        prev = 0
        cnt = 0

        for r in rocks:
            if r - prev < dis:
                cnt += 1
            else:
                prev = r

        return cnt

    ans = 0
    l, r = 0, 1000000000
    rocks.sort()

    while l <= r:
        m = (l + r) // 2
        tmp_cnt = get_count(m)

        if tmp_cnt <= n:
            l = m + 1
        else:
            r = m - 1

    return l - 1
