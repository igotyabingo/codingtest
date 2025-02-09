def solution(n, lost, reserve): 
    # 마지막 제한사항 관련: lost와 reverse의 공통원소는 둘다에서 제외시킨다.
    l = set(lost)-set(reserve)
    r = set(reserve)-set(lost)
    answer = n-len(l)    # 기본적으로 체육수업을 들을 수 있는 학생 수
    
    for i in sorted(l):
        if (i-1) in r:  # * 우선순위를 지정한다.
            answer += 1
            r.remove(i-1)
        elif (i+1) in r:
            answer += 1
            r.remove(i+1)
    
    return answer