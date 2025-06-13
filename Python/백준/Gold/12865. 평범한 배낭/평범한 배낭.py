n, k = map(int, input().split())

lst = []
for _ in range(n):
    w, v = map(int, input().split())
    lst.append((w, v))

# dp[i][j] = i번째 원소까지 고려했을 때, 최대 무게 j인 가방에 넣을 수 있는 가치의 최댓값
# 구하는 것: dp[n-1][k]

dp = [[0]*(k+1) for _ in range(n)]

for i in range(lst[0][0], k+1):
    dp[0][i] = lst[0][1]

# dp[n-1][j-자기무게]+자기가치, dp[n-1][j] 중에 큰 것을 택한다.

for i in range(1, n): # dp[i] 업데이트
    w, v = lst[i]
    for j in range(k+1):
        if j >= w:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][k])