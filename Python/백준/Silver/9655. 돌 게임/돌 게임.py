n = int(input())
# bottom up DP
# dp[i] = 돌이 i개 남아있는 상황에서, 가져가야 할 플레이어가 이길 수 있는지 여부
dp = [False]*(n+1)
dp[0] = False

for i in range(1, n+1):
    for take in [1, 3]:
        if i - take >= 0 and not dp[i-take]:
            # dp[i-take] = False이면 다른 플레이어가 무조건 진다는 뜻
            dp[i] = True
            break

print("SK" if dp[n] else "CY")