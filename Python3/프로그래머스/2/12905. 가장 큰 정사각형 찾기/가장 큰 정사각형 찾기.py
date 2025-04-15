def solution(maps):
    # using dynamic programming, dp[i][j] = (i, j)를 오른쪽 아래 꼭짓점으로 가지는 정사각형의 최대 길이
    dp = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    max_value = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1

                max_value = max(max_value, dp[i][j])
    
    return max_value ** 2