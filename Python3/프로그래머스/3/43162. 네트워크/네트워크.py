from collections import deque

def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    for i in range(n):
        if visited[i]:
            continue
        
        answer += 1
        visited[i] = True
        queue = deque([i])
        
        while queue:
            cur = queue.popleft() # cur 기준 neighbor 탐색
            
            for j in range(n):
                if computers[cur][j] == 1 and not visited[j]:
                    queue.append(j)
                    visited[j] = True
        
    return answer
            
            
            