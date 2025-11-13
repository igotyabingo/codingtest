from collections import defaultdict

def solution(clothes):
    # 각 종류별로 원소 수(a, b) 구하기 -> (a+1)(b+1) -1
    count = defaultdict(int)
    # 일단 한번 순회해야 함
    for cloth in clothes:
        count[cloth[1]] += 1
    
    answer = 1
    for c in count.values():
        answer *= (c+1)
    return answer-1