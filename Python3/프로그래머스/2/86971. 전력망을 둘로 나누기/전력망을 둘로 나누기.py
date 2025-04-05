# 전선 하나씩을 끊어보면서 BFS로 그래프를 생성한다.
from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    count = 1
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
    
    return count

def solution(n, wires):
    answer = n

    for i in range(len(wires)): # 끊을 전선 wires[i]
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n+1)
        group_size = bfs(1, graph, visited)
        other_size = n - group_size
        
        answer = min(answer, abs(group_size-other_size))

    return answer