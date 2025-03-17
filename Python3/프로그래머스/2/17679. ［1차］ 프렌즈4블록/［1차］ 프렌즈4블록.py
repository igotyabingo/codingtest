def solution(m, n, board):
    # 매 라운드마다 board의 모든 칸을 확인한다.
    answer = 0
    board = board[::-1]

    stack = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            stack[i][j] = board[j][i]
    while(True):
        coord = set()
        for i in range(len(stack)-1):
            for j, alp in enumerate(stack[i][:-1]):
                if (i+1 < len(stack) and j+1 < len(stack[i+1]) 
                    and alp == stack[i][j+1] and alp == stack[i+1][j] and alp == stack[i+1][j+1]):  
                    coord.add((i, j))
                    coord.add((i, j+1))
                    coord.add((i+1, j))
                    coord.add((i+1, j+1))

        if not coord: break
        modify(stack, coord)
        answer += len(coord)
    
    return answer

def modify(stack, coord):
    index = dict()
    for i, j in coord:
        if i in index: index[i].append(j)
        else: index[i] = [j]
    for i in index:
        index[i].sort(reverse=True)
        for j in index[i]:
            stack[i].pop(j)