def solution(dirs):
    # 왼쪽, 아래 점좌표와 Vertical/Horizontal의 V, H로 선분을 나타낸다.
    # ex: (x, y, V)
    visited = set()
    x, y = 0, 0 # 업데이트할 현재 위치
    
    for i in dirs:
        if i == 'U' and y != 5:
            visited.add((x, y, 'V'))
            y += 1
        elif i == 'D' and y != -5:
            y -= 1
            visited.add((x, y, 'V'))
        elif i == 'R' and x != 5:
            visited.add((x, y, 'H'))
            x += 1
        elif i == 'L' and x != -5:
            x -= 1
            visited.add((x, y, 'H'))
        
    return len(visited)