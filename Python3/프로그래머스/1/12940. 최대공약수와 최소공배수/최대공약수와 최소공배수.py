import math
def solution(n, m):
    a, b = 0, 0 # return할 최대공약수와 최소공배수
    answer = []
    
    # 대소관계 고정: n < m
    n, m = min(n, m), max(n, m)
    
    # 최대공약수가 될 후보: n의 약수를 리스트에 저장하고 내림차순으로 정렬해서 하나씩 해본다.
    cand = []   
    for i in range(1, math.floor(n**(1/2))+1):
        if(n%i == 0):
            cand.append(i)
            if(n//i != i):
                cand.append(n//i)
    cand.sort(reverse=True)
    
    for i in cand:
        if(m%i == 0):
            a = i
            break
    
    b = a*(n//a)*(m//a)

    return [a, b]