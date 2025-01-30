def solution(a, b, n):
    answer = 0
    
    while(n >= a):
        k = n // a  # 주는 콜라 a개의 묶음 (몫)
        answer += b*k   # k묶음을 주면 b*k개의 병을 다시 받음
        n = n%a + b*k
    
    return answer