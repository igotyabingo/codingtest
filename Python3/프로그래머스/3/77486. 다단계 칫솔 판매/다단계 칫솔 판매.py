from collections import defaultdict

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0 for _ in range(n)]
    name = dict()
    parent = dict() # 인덱스: [부모 인덱스들] 형태로 저장
    
    # name, parent 딕셔너리 초기화
    for i in range(n):
        name[enroll[i]] = i
        if referral[i] != "-":
            parent[i] = [name[referral[i]]] + parent[name[referral[i]]]
        else:
            parent[i] = []
    
    # seller 순환하며 분배, 계산
    for i, s in enumerate(seller):
        # name[s] = seller's index, amount*100 = 판매액
        price = amount[i]*100
        
        for p in [name[s]]+parent[name[s]]:
            val = price // 10
            answer[p] += price - val
            if val == 0:
                break
            price = val
        
    return answer