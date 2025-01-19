# park를 보고 최대 정사각형의 길이를 찾는다. mats는 마지막 확인용

# 1. 전체 칸을 탐색하고 빈칸을 만났을 때마다 그 칸을 중심으로 하는 최대 정사각형의 크기를 저장해나간다. (8방향 모두 확인)
# 2. 정사각형의 배열에서의 특징 -> 같은 행과 열 인덱스를 확인한다
# 3. (i, j) 좌표를 '오른쪽 모서리' 끝으로, 최대 전진 가능 길이를 미리 저장해둔다. ✔️
# -> 세 방향씩 확인

def solution(mats, park):
    ans = 1
    
    # 초기화 
    for i in range(len(park)):
        if(park[i][0] == "-1"):
            park[i][0] = 1
    for j in range(len(park[0])):
        if(park[0][j] == "-1"):
            park[0][j] = 1
    
    for i in range(1, len(park)):
        for j in range(1, len(park[0])):
            if(park[i][j] == "-1"):
                if(type(park[i-1][j]) == int and type(park[i][j-1]) == int and type(park[i-1][j-1]) == int):
                    park[i][j] = min(park[i-1][j-1], park[i-1][j], park[i][j-1]) + 1
                    ans = max(ans, park[i][j])
                else:
                    park[i][j] = 1
    
    answer = -1
    for mat in sorted(mats):
        if(mat <= ans):
            answer = mat
        else:
            break
    return(answer)
