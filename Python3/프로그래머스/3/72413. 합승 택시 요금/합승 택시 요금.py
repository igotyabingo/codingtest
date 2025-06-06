def solution(n, s, a, b, fares):
    # 1. 각 지점에서 각 지점 까지의 최단거리를 계산: floyd-warshall 알고리즘
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for i, j, d in fares:
        dist[i-1][j-1] = d
        dist[j-1][i-1] = d
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    
    answer = float('inf')
    for k in range(n):
        answer = min(answer, dist[s-1][k]+dist[k][a-1]+dist[k][b-1])    
    
    return answer