import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    answer = float('inf')
    # 1. 각 지점에서 각 지점 까지의 최단거리를 계산: 각 지점에 대해 다익스트라 알고리즘을 사용
    graph = defaultdict(list)
    for i, j, d in fares:
        graph[i].append((j, d))
        graph[j].append((i, d))
    
    distance = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        distance[i][i] = 0
        queue = []
        heapq.heappush(queue, (i, 0))
        
        while queue:
            node, d = heapq.heappop(queue)
            if distance[i][node] >= d:
                for neighbor, cost in graph[node]:
                    if distance[i][neighbor] > cost + d:
                        distance[i][neighbor] = cost + d
                        heapq.heappush(queue, (neighbor, cost+d))
    
    for i in range(1, n+1):
        answer = min(answer, distance[s][i]+distance[i][a]+distance[i][b])
   
    return answer