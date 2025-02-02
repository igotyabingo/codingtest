def solution(n):
    # n=2는 따로 처리한다. 
    if (n==2):
        return 1
    else:
        answer = 1  # 2는 일단 포함한다.
        
        for i in range(3, n+1, 2):
            a = True
            # 모든 홀수에 대해 소수인지를 체크한다.
            for j in range(3, int(i**(1/2))+1, 2):
                if(i%j == 0):
                    a = False
                    break
            if a:
                answer += 1
                
        return answer
