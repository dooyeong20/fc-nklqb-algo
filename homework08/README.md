# Homework #8

프로그래머스 징검다리 문제 풀이  
[징검다리](https://programmers.co.kr/learn/courses/30/lessons/43236)

## Source File

[solution.py](src/solution.py)

## Code

```python
def solution(distance, rocks, n):
    # 주어진 distance를 징검다리에 적용했을 때, 몇 개의 징검다리를 없애야 하는지 리턴해줌
    def get_count(dis):
        prev = 0
        cnt = 0

        for r in rocks:
            if r - prev < dis:  # 징검 다리의 거리가 기준보다 가깝다면, 제거(cnt + 1)
                cnt += 1
            else:
                prev = r    # 거리가 충분하다면, 그냥 진행

        return cnt

    ans = 0
    l, r = 0, 1000000000
    rocks.sort()    # 징검다리 사이의 거리를 순차적으로 구해주기 위해 정렬

    while l <= r:
        m = (l + r) // 2
        tmp_cnt = get_count(m)

        if tmp_cnt <= n:    # 만약 없앨 징검다리가 작거나 같다면, 거리를 증가하며 진행
            l = m + 1
        else:
            r = m - 1       # 만약 없앨 징검다리가 많다면 거리를 좁히며 진행

    return l - 1
```
