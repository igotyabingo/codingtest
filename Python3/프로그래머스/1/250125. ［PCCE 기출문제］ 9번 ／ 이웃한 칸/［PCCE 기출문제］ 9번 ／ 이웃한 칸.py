def solution(board, h, w):
    count = 0
    color = board[h][w]
    lst = []
    
    # 일반적인 h, w에 대해 확인해야 할 칸 4개: (h-1, w), (h+1, w), (h, w-1), (h, w+1)
    # 특수경우: 테두리 직사각형
    l = len(board)
    if(h-1 >= 0):
        lst.append(board[h-1][w])
    if(h+1 < l):
        lst.append(board[h+1][w])
    if(w-1 >= 0):
        lst.append(board[h][w-1])
    if(w+1 < l):
        lst.append(board[h][w+1])

    return lst.count(color)