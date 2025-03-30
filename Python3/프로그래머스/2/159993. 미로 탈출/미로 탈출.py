def solution(maps):
    h, w = len(maps), len(maps[0])
    answer = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                exit = (i, j)

    # 1. start -> lever
    queue = [[start, 0]]
    visited = [[False]*w for _ in range(h)]
    target = False

    while(queue):
        (x, y), count = queue.pop(0)
        if (x, y) == lever: 
            answer += count
            target = True
            break

        if x > 0 and not visited[x-1][y] and maps[x-1][y] != "X": # 위로 이동
            queue.append([(x-1, y), count+1])
            visited[x-1][y] = True
        if x < h-1 and not visited[x+1][y] and maps[x+1][y] != "X": # 아래로 이동
            queue.append([(x+1, y), count+1])
            visited[x+1][y] = True
        if y > 0 and not visited[x][y-1] and maps[x][y-1] != "X": # 왼쪽으로 이동
            queue.append([(x, y-1), count+1])
            visited[x][y-1] = True
        if y < w-1 and not visited[x][y+1] and maps[x][y+1] != "X": # 오른쪽으로 이동
            queue.append([(x, y+1), count+1])
            visited[x][y+1] = True

    if not target: return -1

    # 2. lever -> exit
    queue = [[lever, 0]]
    visited = [[False]*w for _ in range(h)]
    target = False

    while(queue):
        (x, y), count = queue.pop(0)
        if (x, y) == exit: 
            answer += count
            target = True
            break

        if x > 0 and not visited[x-1][y] and maps[x-1][y] != "X": # 위로 이동
            queue.append([(x-1, y), count+1])
            visited[x-1][y] = True
        if x < h-1 and not visited[x+1][y] and maps[x+1][y] != "X": # 아래로 이동
            queue.append([(x+1, y), count+1])
            visited[x+1][y] = True
        if y > 0 and not visited[x][y-1] and maps[x][y-1] != "X": # 왼쪽으로 이동
            queue.append([(x, y-1), count+1])
            visited[x][y-1] = True
        if y < w-1 and not visited[x][y+1] and maps[x][y+1] != "X": # 오른쪽으로 이동
            queue.append([(x, y+1), count+1])
            visited[x][y+1] = True
        

    if not target: return -1

    return answer