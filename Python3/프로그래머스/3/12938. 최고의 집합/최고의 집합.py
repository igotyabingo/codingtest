def solution(n, s):
    if n > s: return [-1]
    answer = []
    # n%s 개는 s//n+1, 나머지는 s//n로 채우기

    for _ in range(n-s%n):
        answer.append(s//n)
    
    for _ in range(s%n):
        answer.append(s//n+1)
    
    return answer