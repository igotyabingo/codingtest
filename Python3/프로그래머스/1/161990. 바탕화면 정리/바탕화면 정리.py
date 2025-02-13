def solution(wallpaper):
    # 2차원의 문자열 배열 wallpaper에 #인 칸에 파일이 있고, .인 칸에는 비어있다    
    # '행' 의 최소 최대, '열'의 최소 최대를 행 / 열 독립적으로 찾는다.    
    minx, maxx = len(wallpaper), -1
    miny, maxy = len(wallpaper[0]), -1
    
    for i, col in enumerate(wallpaper):
        for j, row in enumerate(col):
            if row == "#":
                minx = min(i, minx)
                maxx = max(i+1, maxx)
                miny = min(j, miny)
                maxy = max(j+1, maxy)
    
    return [minx, miny, maxx, maxy]