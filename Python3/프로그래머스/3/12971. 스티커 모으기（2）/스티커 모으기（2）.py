def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    # Dynamic Programming: 각 인덱스에 대해 뽑는 경우와 뽑지 않는 경우 두가지를 memoization
    # 현재 인덱스를 뽑는 경우 -> {이전 인덱스를 뽑지 않는 경우}+{현재 인덱스 값}
    # 현재 인덱스를 뽑지 않는 경우 -> max({이전 인덱스를 뽑지 않는 경우}, {이전 인덱스를 뽑는 경우})
    # 마지막 인덱스는 0번째 인덱스를 뽑은 경우 반드시 뽑을 수 없음을 고려하기 위해 0번째 인덱스를 뽑는 경우와 뽑지 않는 경우를 처음부터 나눠서 dp를 2번 실행해야 함.
    
    # dp[n][0] = n번째 인덱스를 뽑지 않는 경우, dp[n][1] = n번째 인덱스를 뽑는 경우
    dp = [[0, 0] for _ in range(len(sticker))]
    answer = 0

    # 1. 0번째 인덱스를 뽑지 않은 경우 -> 마지막 인덱스를 뽑을 수 있음
    dp[0] = [0, 0]
    # bottom up
    for n in range(1, len(sticker)):
        dp[n][0] = max(dp[n-1][0], dp[n-1][1])
        dp[n][1] = dp[n-1][0] + sticker[n]
    answer = max(dp[-1])
    
    # 2. 0번째 인덱스를 뽑은 경우 -> 1번째 못 뽑음, 마지막 인덱스 못 뽑음
    dp[2] = [sticker[0], sticker[0]+sticker[2]]
    # bottom up
    for n in range(3, len(sticker)-1):
        dp[n][0] = max(dp[n-1][0], dp[n-1][1])
        dp[n][1] = dp[n-1][0] + sticker[n]
    
    return max(dp[-2]+[answer])