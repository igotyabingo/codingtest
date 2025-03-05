def solution(maps):
    # BFS 를 사용하여 가능한 경로를 모두 탐색하고 최소 이동 칸수를 구한다.
    target = (len(maps)-1, len(maps[0])-1)
    visited = [[1000000]*(target[1]+1) for _ in range(target[0]+1)]
    visited[0][0] = 1
    queue = [(0, 0, 1)]
    
    while(queue):
        dx, dy, l = queue.pop(0)
        for (x, y) in [(dx+1, dy), (dx, dy+1), (dx-1, dy), (dx, dy-1)]:
            # 적 팀의 진영에 도착한 경우
            if ((x, y)==target):
                return l+1
            elif (0<=x<=target[0] and 0<=y<=target[1] and maps[x][y]==1 and  
                 l+1 < visited[x][y]):
                # 경계 내부이고 이동할 수 있는 칸이면
                queue.append((x, y, l+1))
                visited[x][y] = l+1
    return -1 