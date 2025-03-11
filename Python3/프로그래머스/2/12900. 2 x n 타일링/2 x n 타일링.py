def solution(n):
    # f(n) = f(n-1) + f(n-2) 의 관계식을 만족함
    # swap 사용
    x, y = 1, 2
    
    for i in range(n-2):
        x, y = y, (x+y)%1000000007

    return y