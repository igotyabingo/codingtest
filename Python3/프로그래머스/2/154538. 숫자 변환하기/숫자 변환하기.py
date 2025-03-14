def solution(x, y, n):
    # BFS를 사용한다: 각 분기에서 3가지 연산 / 최단거리 찾기
    candidates = [(y, 0)] # 현재 진행 중인 경로들을 저장할 queue
    
    # x -> y로 곱셈을 수행하는 것보다 y -> x에서 떨어지지 않는 나눗셈을 확인하면 훨씬 시간을 감소할 수 있다.
    while(candidates):
        now, l = candidates.pop(0)
        if now == x:
            return l
        
        if (now-n) == x:
            return l+1
        elif (now-n) > x:
            candidates.append((now-n, l+1))
        
        if now%2 == 0:
            if now//2 == x:
                return l+1
            elif now//2 > x:
                candidates.append((now//2, l+1))
        
        if now%3 == 0:
            if now//3 == x:
                return l+1
            elif now//3 > x:
                candidates.append((now//3, l+1))
    
    return -1