from collections import deque

def solution(board):
    a, b, c, d = 0, 0, 0, 0

    # 1. R과 G의 인덱스 확인: (a, b) -> (c, d)
    tmp_count = 0 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                a, b = i, j
                tmp_count += 1
            elif board[i][j] == 'G':
                c, d = i, j
                tmp_count += 1
                # G의 4방향 모두가 모서리도 아니고 D도 아니면 바로 -1을 리턴한다.
                if c!=0 and c!=len(board)-1 and d!=0 and d!=len(board[0])-1:
                    if board[c-1][d]!='D' and board[c+1][d]!='D':
                        if board[c][d-1]!='D' and board[c][d+1]!='D':
                            return -1
            if tmp_count == 2:
                break
    
    
    # 2. BFS로 탐색하며 이동, 제일 먼저 도달한 게 최단거리인 답임
    # 이전 방향이 좌/우 였다면 상/하로만 이동, 상/하 였다면 좌/우로만 이동 확인: 상/하 -> -1, 좌/우 -> 1
    queue = deque([(a, b, 0, 0)])
    visited = set()
    
    while queue:
        x, y, d, count = queue.popleft()
        
        if d<=0: # 좌/우로 이동 확인
            tmp = y
            while tmp>-1 and board[x][tmp]!='D':
                tmp -= 1 
            if board[x][tmp+1] == 'G':
                return count+1
            if tmp+1 != y and (x, tmp+1, 'L') not in visited:
                queue.append((x, tmp+1, 1, count+1))
                visited.add((x, tmp+1, 'L'))

            tmp = y
            while tmp<len(board[0]) and board[x][tmp]!='D':
                tmp += 1
            if board[x][tmp-1] == 'G':
                return count+1
            if tmp-1 != y and (x, tmp-1, 'R') not in visited:
                queue.append((x, tmp-1, 1, count+1))
                visited.add((x, tmp-1, 'R'))
            
        if d>=0: # 상/하로 이동 확인
            tmp = x
            while tmp>-1 and board[tmp][y]!='D':
                tmp -= 1
            if board[tmp+1][y] == 'G':
                return count+1
            if tmp+1 != x and (tmp+1, y, 'U') not in visited:
                queue.append((tmp+1, y, -1, count+1))
                visited.add((tmp+1, y, 'U'))
            
            tmp = x
            while tmp<len(board) and board[tmp][y]!='D':
                tmp += 1
            if board[tmp-1][y] == 'G':
                return count+1
            if tmp-1 != x and (tmp-1, y, 'D') not in visited:
                queue.append((tmp-1, y, -1, count+1))
                visited.add((tmp-1, y, 'D'))
    return -1            