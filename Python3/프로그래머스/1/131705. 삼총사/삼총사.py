def solution(number):
    l = len(number)
    ans = 0
    
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if(number[i]+number[j]+number[k] == 0):
                    ans += 1
                    
    return ans