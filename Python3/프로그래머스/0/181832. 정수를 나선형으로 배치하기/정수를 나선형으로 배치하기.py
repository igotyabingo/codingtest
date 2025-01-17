def solution(n):
    answer = [[0]*n for _ in range(n)] 
    # 네 방향 움직임을 반복한다.
    cnt = 1
    round = 0
    while(True): 
        # 1. 첫번째 -> 방향 
        for i in range(n-2*round):
            answer[round][round+i] = cnt
            cnt += 1
            if(cnt == n*n +1):
                return answer
        # 2. 두번째: 아래 방향
        for i in range(n-1-2*round):
            answer[round+i+1][n-1-round] = cnt
            cnt += 1
            if(cnt == n*n +1):
                return answer
        # 3. 세번째: <- 방향
        for i in range(n-1-2*round):
            answer[n-1-round][n-2-round-i] = cnt
            cnt += 1
            if(cnt == n*n +1):
                return answer
        # 4. 네번째: 위 방향
        for i in range(n-2-2*round):  
            answer[n-2-i-round][round] = cnt
            cnt += 1
            if(cnt == n*n +1):
                return answer
        round += 1