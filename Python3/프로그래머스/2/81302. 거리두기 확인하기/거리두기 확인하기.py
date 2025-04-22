def solution(places):
    answer = []
    
    for place in places:
        boolean = True
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    # 맨해튼 거리가 2 이하에 있는 좌표들(중 P)을 모두 확인한다.
                    # 1. 맨해튼 거리가 1이면 예외가 없다.
                    for dx, dy in [(0, 1), (1, 0)]:
                        if x+dx < 5 and y+dy < 5 and place[x+dx][y+dy] == 'P':
                            boolean = False
                    # 2. 맨해튼 거리가 2일때는 예외 경우가 몇가지 존재한다.
                    for dx, dy in [(2, 0), (0, 2)]:
                        if x+dx < 5 and y+dy < 5 and place[x+dx][y+dy] == 'P' and place[x+dx//2][y+dy//2] != 'X':
                            boolean = False
                    # 2-1. (dx, dy) = (1, 1)
                    if x+1 < 5 and y+1 < 5 and place[x+1][y+1] == 'P' and not (place[x+1][y] == 'X' and place[x][y+1] == 'X'):
                        boolean = False
                    # !! 2-2. (dx, dy) = (1, -1)
                    if x+1 < 5 and y-1 > -1 and place[x+1][y-1] == 'P' and not (place[x+1][y] == 'X' and place[x][y-1] == 'X'):
                        boolean = False
                        
        if boolean: answer.append(1)
        else: answer.append(0)
    
    return answer