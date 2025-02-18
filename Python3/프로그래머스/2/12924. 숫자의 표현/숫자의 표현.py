def solution(n):
    answer = 1
    for i in range(n, 1, -1):
        if(n>i*(i-1)/2 and (n-i*(i-1)/2)%i==0):
            answer += 1
    return answer