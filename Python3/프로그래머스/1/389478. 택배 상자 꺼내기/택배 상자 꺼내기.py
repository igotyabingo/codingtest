def solution(n, w, num):
    # 해당 열만 쌓으면 되고 다 쌓을 필요가 없다. 수학 문제로 생각하면 쉽다.
    answer = 0
    
    if(num%w == 0):
        c = 1
    else:
        c = (w-num%w)*2 + 1

    i = 1  
    up = num
    
    while(up <= n):
        if(i%2 == 0):
            up += 2*w-c
        else:
            up += c
        i += 1
        answer += 1
    
    return answer 