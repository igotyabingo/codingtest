def solution(rows, columns, queries):
    answer = []
    board = [[0]*columns for _ in range(rows)]

    k = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = k
            k += 1

    for query in queries:
        a, b, c, d = query
        # 각 테두리에 새로 들어갈 원소를 미리 작성한다.
        w1, h2 = [board[a][b-1]], [board[a-1][d-2]]
        w2, h1 = [], [] # 마지막에 추가

        for y in range(b-1, d-1):
            w1.append(board[a-1][y])
            w2.append(board[c-1][y+1])
        w2.append(board[c-2][d-1])

        for x in range(a-1, c-1):
            h2.append(board[x][d-1])
            h1.append(board[x+1][b-1])
        h1.append(board[c-1][b])

        board[a-1][b-1:d] = w1
        board[c-1][b-1:d] = w2
        for x in range(a-1, c):
            board[x][b-1] = h1[x-(a-1)]
            board[x][d-1] = h2[x-(a-1)]

        answer.append(min(min(h1), min(h2), min(w1), min(w2)))

    return answer