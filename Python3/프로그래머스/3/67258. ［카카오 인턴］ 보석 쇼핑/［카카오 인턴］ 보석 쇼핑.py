from collections import Counter

def solution(gems):
    N = len(set(gems))

    # 1. 0부터 시작했을 때 최소 길이의 집합 찾기 [:k+1]
    base = set()
    for i in range(len(gems)):
        base.add(gems[i])
        if len(base) == N:
            k = i
            break
    val, ans = k+1, [1, k+1]

    count = dict(Counter(gems[:k+1]))

    # 2. 시작 인덱스를 하나씩 오른쪽으로 옮김
    for i in range(1, len(gems)):
        if count[gems[i-1]] == 1:
            count[gems[i-1]] = 0
            pos = True
            for j in range(k+1, len(gems)):
                count[gems[j]] += 1
                if gems[j] == gems[i-1]:
                    pos = False
                    k = j
                    if j-i+1 < val:
                        val, ans = j-i+1, [i+1, j+1]
                    break
            if pos: return ans

        else:
            count[gems[i-1]] -= 1
            if k-i+1 < val:
                val = k-i+1
                ans = [i+1, k+1]        

    return ans