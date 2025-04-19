def solution(land):
    h, w = len(land), len(land[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    sums = [0 for _ in range(w)]

    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and not visited[i][j]:
                # 기준점 선택, 상하좌우를 모두 확인한다.
                queue, tmp = [(i, j)], 1
                rows = set([j])
                visited[i][j] = True

                while(queue):
                    x, y = queue.pop(0)
                    for dx, dy in directions:
                        if -1 < x+dx < h and -1 < y+dy < w and land[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                            visited[x+dx][y+dy] = True
                            rows.add(y+dy)
                            tmp += 1
                            queue.append((x+dx, y+dy))
                for r in rows:
                    sums[r] += tmp    
    
    return max(sums)