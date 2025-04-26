def solution(m, n, puddles):
    # 0-based, (n+1)*(m+1) 크기의 격자에 (1, 1)에서 시작해서 (n, m)까지 간다고 생각하자.
    # puddles 의 각 원소도 x, y 자리 변경해서 생각해야 함
    # BFS로 풀면 시간초과, DP 사용
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            elif [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
    
    return dp[n][m]