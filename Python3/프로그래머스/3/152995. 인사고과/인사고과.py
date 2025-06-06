from collections import Counter

def solution(scores):
    # 사원별 -> 근무 태도 점수, 동료 평가 점수
    # 1. 인센티브를 받지 못하는 경우  **
    # 2. 그렇지 않은 경우 = 두 점수의 합 순서대로 석차를 매긴다. -> Counter 객체 쓰면 됨
    wan = scores[0]
    ranks = []
    scores.sort(reverse=True)
    y, tmp = -1, -1
    
    for i in range(len(scores)):
        a, b = scores[i]
        tmp = max(b, tmp)

        if b >= y:
            ranks.append(a+b)
        elif [a, b] == wan: 
            return -1
            
        if i < len(scores)-1 and a > scores[i+1][0]:
            y = max(y, tmp)
            tmp = -1
    
    ranks.sort(reverse=True)
    ranks = dict(Counter(ranks))
    
    i = 0
    for key in sorted(ranks.keys(), reverse=True):
        if key == sum(wan):
            return i+1
        i += ranks[key]