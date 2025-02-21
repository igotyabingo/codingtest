def solution(n):
    # 2씩 나누어가면서 몫이 홀수 일때마다 1번씩 점프한다.
    ans = 1
    while(n!=1):
        if(n%2 == 1):
            n -= 1
            ans += 1
        else:
            n /= 2

    return ans