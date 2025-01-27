def solution(n):
    # 10진법 -> 3진법으로 변환
    ans = ''
    while(n > 0):
        n, k = n//3, n%3    
        ans += str(k)
    
    # 마지막에 3진법 -> 10진법으로 변환하여 리턴한다.
    return int(ans,3)