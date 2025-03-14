def solution(x, y, n):
    # BFS를 사용한다: 각 분기에서 3가지 연산 / 최단거리 찾기
    candidates = [(x, 0)] # 현재 진행 중인 경로들을 저장할 queue
    
    if (x==y): return 0
    
    # x -> y로 곱셈을 수행하는 것보다 y -> x에서 떨어지지 않는 나눗셈을 확인하면 훨씬 시간을 감소할 수 있다.
    # 또는 visited 배열을 사용한다. (더 적은 횟수로 이미 그 숫자에 도달한 경우가 있는지)
    visited = [False] * 1000001
    
    while(candidates):
        now, l = candidates.pop(0)
        
        for updated in [now+n, now*2, now*3]:
            if updated == y:
                return l+1
            elif updated < y and not visited[updated]:
                visited[updated] = True
                candidates.append((updated, l+1))
            
    return -1