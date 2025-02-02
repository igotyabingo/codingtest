def solution(k, m, score):
    answer = 0
    
    # 내림차순으로 정렬한다
    score.sort(reverse=True)
    
    for i in range(m-1, len(score), m):
        answer += score[i]*m
    
    return answer