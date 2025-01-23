def solution(t, p):
    ans = 0
    l = len(p)
    
    for i in range(len(t)-len(p)+1):
        if(int(t[i:i+l])<=int(p)):
            ans += 1

    return ans