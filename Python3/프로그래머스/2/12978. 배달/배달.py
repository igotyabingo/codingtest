def solution(N, road, K):
    # 1번 ~ N번 마을에 대한 Dijkstra Algorithm을 수행한다.
    visited = [False for _ in range(N)]
    count = 0
    distance = [float('inf') for _ in range(N)]
    filter = dict()
    roads = dict()
    answer = 0 

    for r in road:
        x, a, b = r
        
        if x in roads:
            roads[x].append((a, b))
        else:
            roads[x] = [(a, b)]
        
        if a in roads:
            roads[a].append((x, b))
        else:
            roads[a] = [(x, b)]
    
    target = 1
    distance[0] = 0
    filter[1] = 0
    while(count < N):
        candidates = roads[target]
        for c in candidates:
            x, y = c
            if distance[x-1] > distance[target-1] + y:
                distance[x-1] = distance[target-1]+y
                filter[x] = distance[x-1]
        visited[target-1] = True
        count += 1
        # 아직 방문하지 않은 노드 중 거리가 최소인것을 다음 타겟으로 삼음
        target = min(filter, key=filter.get)
        del filter[target]
    
    for d in distance:
        if d <= K:
            answer += 1

    return answer