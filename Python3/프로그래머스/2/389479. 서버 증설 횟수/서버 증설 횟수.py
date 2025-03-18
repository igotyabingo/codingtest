from collections import deque
def solution(players, m, k):
    # deque를 이용해 sliding window 구현 
    window = deque(maxlen = k)
    for _ in range(k):
        window.append(0)

    answer = 0 
    for p in players:
        window.append(0)
        tmp = p // m
        s = sum(window)
        if s < tmp:
            window[-1] = tmp - s
            answer += tmp - s

    return answer