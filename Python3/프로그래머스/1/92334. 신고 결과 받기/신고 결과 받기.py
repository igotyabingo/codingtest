def solution(id_list, report, k):
    # 사용자 이름과 아이디 매핑
    user = {}
    for i, j in enumerate(id_list):
        user[j] = i
    
    answer = [0 for _ in range(len(id_list))]
        
    reported = {}
    for i in report:
        b, a = i.split()
        if a not in reported:
            reported[a] = [b]        
        elif b not in reported[a]:
            reported[a].append(b)
    
    for i in reported:
        if len(reported[i]) >= k:
            for j in reported[i]:
                answer[user[j]] += 1

    return answer