from collections import defaultdict

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0 for _ in range(n)]
    name = dict()
    parent = [-1 for _ in range(n)] # 인덱스: [부모 인덱스들] 형태로 저장
    
    # name, parent 딕셔너리 초기화
    for i in range(n):
        name[enroll[i]] = i
        if referral[i] != "-":
            parent[i] = name[referral[i]]
    
    # seller 순환하며 분배, 계산
    for i, s in enumerate(seller):
        target = name[s]
        price = amount[i] * 100
        while parent[target] != -1:
            val = price // 10
            answer[target] += price - val
            
            target = parent[target]
            price = val
            if val == 0:
                break
                
        answer[target] += price - price // 10
        
    return answer