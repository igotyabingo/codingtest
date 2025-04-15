def solution(maps):
    result = []
    h, w = len(maps), len(maps[0])
    visited = [[False for _ in range(w)] for _ in range(h)]

    for x in range(h):
        for y in range(w):
            # '기준' 좌표, 상하좌우 모두 고려해야 함(좌, 상 도)
            if maps[x][y]!='X' and not visited[x][y]:
                visited[x][y] = True
                sum, queue = int(maps[x][y]), []
                if x+1 < h and maps[x+1][y]!='X' and not visited[x+1][y]:
                    queue.append((x+1, y))
                    visited[x+1][y] = True
                    sum += int(maps[x+1][y])
                if y+1 < w and maps[x][y+1]!='X' and not visited[x][y+1]:
                    queue.append((x, y+1))
                    visited[x][y+1] = True
                    sum += int(maps[x][y+1])
                if x-1 > -1 and not visited[x-1][y] and maps[x-1][y]!='X':
                    queue.append((x-1, y))
                    visited[x-1][y] = True
                    sum += int(maps[x-1][y])
                if y-1 > -1 and not visited[x][y-1] and maps[x][y-1]!='X':
                    queue.append((x, y-1))
                    visited[x][y-1] = True
                    sum += int(maps[x][y-1])

                while(queue):
                    a, b = queue.pop(0)
                    if a+1 < h and maps[a+1][b]!='X' and not visited[a+1][b]:
                        queue.append((a+1, b))
                        visited[a+1][b] = True
                        sum += int(maps[a+1][b])
                    if b+1 < w and maps[a][b+1]!='X' and not visited[a][b+1]:
                        queue.append((a, b+1))
                        visited[a][b+1] = True
                        sum += int(maps[a][b+1])
                    if a-1 > -1 and not visited[a-1][b] and maps[a-1][b]!='X':
                        queue.append((a-1, b))
                        visited[a-1][b] = True
                        sum += int(maps[a-1][b])
                    if b-1 > -1 and not visited[a][b-1] and maps[a][b-1]!='X':
                        queue.append((a, b-1))
                        visited[a][b-1] = True
                        sum += int(maps[a][b-1])

                result.append(sum)
    return sorted(result) if result else [-1]