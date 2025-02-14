def solution(park, routes):
    # 경계 확인 위한 상수
    H, W = len(park), len(park[0])
    # 좌표 계산 위한 dic
    dic = {'E': (0, 1), 'S': (1, 0), 'N': (-1, 0), 'W': (0, -1)}
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                # 강아지의 현재 위치 저장할 변수
                x = i
                y = j
                break
                
    for i in routes:
        op, n = i.split()
        n = int(n)
        # 좌표 계산
        x1, y1 = dic[op]
        x1 = x+x1*n
        y1 = y+y1*n
        
        # 경계 및 장애물 확인
        if(x1<H and x1>-1 and y1<W and y1>-1 and isBlocked(park, op, n, x, y)):
            x, y = x1, y1
            print(x, y)
            
    return [x, y]

# 움직이는 동안에 장애물 있는지 확인하는 함수
def isBlocked(park, op, n, x, y):
    if(op == 'N'):
        for i in range(1, n+1):
            if(park[x-i][y] == 'X'):
                return False
        return True
    if(op == 'S'):
        for i in range(1, n+1):
            if(park[x+i][y] == 'X'):
                return False
        return True
    if(op == 'W'):
        for i in range(1, n+1):
            if(park[x][y-i] == 'X'):
                return False
        return True
    if(op == 'E'):
        for i in range(1, n+1):
            if(park[x][y+i] == 'X'):
                return False
        return True
    