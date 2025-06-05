# 재귀함수로 구현시 시간 초과, bottom up DP를 사용한다.
def solution(n, money):    
    dp = [0] * (n+1) # dp[i]: i원을 만드는 방법
    dp[0] = 1
    
    for coin in money:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
    
    return dp[n]%1000000007