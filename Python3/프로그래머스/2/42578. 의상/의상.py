from collections import defaultdict

def solution(clothes):
    answer = 1
    count = defaultdict(int)
    # 의상의 종류로 dict 구성: count만
    for _, b in clothes:
        count[b] += 1
    
    for num in count.values():
        answer *= (num+1)
    return answer-1