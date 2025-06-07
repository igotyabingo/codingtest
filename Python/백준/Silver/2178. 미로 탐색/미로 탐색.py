n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

# bfs 사용
queue = [(0, 0, 1)]
visited = set()

while queue:
    x, y, d = queue.pop(0)
    if x == len(board)-1 and y == len(board[0])-1:
        print(d)
        break

    if 0 <= x < len(board)-1:
        if board[x+1][y] == 1 and (x+1, y) not in visited:
            queue.append((x+1, y, d+1))
            visited.add((x+1, y))
    
    if 0 < x <= len(board)-1:
        if board[x-1][y] == 1 and (x-1, y) not in visited:
            queue.append((x-1, y, d+1))
            visited.add((x-1, y))
    
    if 0 <= y < len(board[0])-1 and (x, y+1) not in visited:
        if board[x][y+1] == 1:
            queue.append((x, y+1, d+1))
            visited.add((x, y+1))

    if 0 < y <= len(board[0])-1 and (x, y-1) not in visited and board[x][y-1] == 1:
        queue.append((x, y-1, d+1))
        visited.add((x, y-1))
    