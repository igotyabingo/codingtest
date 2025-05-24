from collections import defaultdict, deque
# 간선 가중치가 동일한 그래프에서 최단 거리 문제는 무조건 BFS를 사용하는 것이 좋습니다.

def solution(n, vertex):
    graph = defaultdict(list)

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    distance = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    distance[1], visited[1] = 0, True
    queue = deque([1])

    while queue:
        target = queue.popleft()
        for neighbor in graph[target]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[target]+1
                queue.append(neighbor)
    
    return distance.count(max(distance))