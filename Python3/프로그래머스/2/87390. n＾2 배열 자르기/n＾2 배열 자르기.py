def solution(n, left, right):
    answer = []
    
    for i in range(left+1, right+2):
        a, b = i//n + 1, i%n
        if b==0: 
          b=n
          a-=1
        answer.append(max(a, b))
            
    return answer

solution(4, 0, 15)