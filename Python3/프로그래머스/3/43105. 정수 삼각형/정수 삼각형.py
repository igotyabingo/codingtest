def solution(triangle):
    # bottom up DP
    dp = triangle
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]

    return dp[0][0]