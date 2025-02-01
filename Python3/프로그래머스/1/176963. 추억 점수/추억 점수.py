def solution(name, yearning, photo):
    answer = []
    
    # 사람 이름을 key로 하고 해당 사람의 그리움 점수를 value로 가지는 dictionary를 생성한다.
    dic = {}
    for i in range(len(name)):
        dic[name[i]] =  yearning[i]
    
    # 각 photo마다 그리움 점수를 계산하여 answer에 순서대로 추가한다.
    for p in photo: 
        a = 0
        for j in p:
            if j in dic:
                a += dic[j]
        answer.append(a)
        
    return answer