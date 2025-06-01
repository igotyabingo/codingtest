from collections import deque

def solution(board):
    N = len(board)
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()

    # 방향: 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for dir in [1, 3]:  # 하(1), 우(3) 로 시작
        visited[0][0][dir] = 0
        queue.append((0, 0, dir, 0))

    while queue:
        x, y, dir, cost = queue.popleft()

        for ndir in range(4):
            nx = x + dx[ndir]
            ny = y + dy[ndir]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                ncost = cost + 100 if dir == ndir else cost + 600

                if visited[nx][ny][ndir] > ncost: # 같은 방향으로 이미 그 지점을 통과했다면 그것보다 최소 거리여야 의미가 있음
                    visited[nx][ny][ndir] = ncost
                    queue.append((nx, ny, ndir, ncost))

    return min(visited[N-1][N-1])