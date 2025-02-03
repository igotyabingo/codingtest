def solution(n, m, section):
    answer = 0
    pos = section[0]
    
    # set에 남아있는 원소가 없을 때 까지
    for i in section[1:]:
        if(pos+m <= i):
            # update
            pos = i
            answer += 1
            
    return answer+1
