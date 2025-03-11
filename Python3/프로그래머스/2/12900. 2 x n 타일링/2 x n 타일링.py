def solution(n):
    # f(n) = f(n-1) + f(n-2) 의 관계식을 만족함
    answer = [0, 1, 2]
    
    for i in range(3, n):
        answer.append((answer[i-1]+answer[i-2])%1000000007)

    return (answer[n-1]+answer[n-2])%1000000007