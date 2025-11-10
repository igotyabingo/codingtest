def solution(participant, completion):
    # set으로 변환 후 차집합 구하는 것 불가능: 동명이인이 있을 수 있음
    # 각 이름 별로 count 확인
    count = dict()
    for p in participant:
        if p in count: 
            count[p] += 1
        else:
            count[p] = 1
    
    for c in completion:
        count[c] -= 1
    
    for c in count:
        if count[c] == 1:
            return c