def solution(routes):
    answer, tmp = 0, -30001
    routes.sort(key = lambda x:x[1])
    
    while routes:
        x, y = routes.pop(0)
        if x > tmp:
            tmp = y
            answer += 1
        
    return answer