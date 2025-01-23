def solution(d, budget):
    answer = 0
    # 부서의 '개수'를 최대화: 신청액이 작은 부서부터 지원한다.
    d.sort()
    
    for i in d:
        budget -= i
        if(budget >= 0):
            answer += 1
        else:
            return answer
    return answer
