def solution(n):
    # 앞선 계산값들을 배열에 저장해둔다. (시간 복잡도)
    fib = [0, 1, 1, 2]
    for i in range(4, n+1):
        fib.append(fib[i-1]+fib[i-2])
    
    return fib[n]%1234567