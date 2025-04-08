def solution(n):
    answer = []
    entire = [[] for _ in range(n)]
    
    for i in range(n):
        entire[i] = [i+1] + [0 for _ in range(i)]

    i, j = 0, n+1
    count = n-1
    
    while(j <= n*(n+1)//2):
        k = i // 3 + 1
        if i%3 == 0: # 오른쪽 방향
            for idx, val in enumerate(range(j, j+count)):
                entire[-k][k+idx] = val
        elif i%3 == 1: # 위쪽 방향
            for idx, val in enumerate(range(j, j+count)):
                entire[-(k+idx+1)][-k] = val
        else: 
            for idx, val in enumerate(range(j, j+count)):
                entire[2*k+idx][k] = val
        i += 1
        j = val+1
        count -= 1
    
    for e in entire:
        for f in e:
            answer.append(f)
            
    return answer