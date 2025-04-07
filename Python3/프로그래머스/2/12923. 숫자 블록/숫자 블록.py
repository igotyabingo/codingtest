def solution(begin, end):
    answer = []
    
    for n in range(begin, end+1):
        if n < 10000000:
            if n == 1:
                answer.append(0)
            else:        
                for k in range(n-1, 0, -1):
                    if n%k == 0:
                        answer.append(k)
                        break
        else:
            if n == 10000000:
                answer.append(10000000)
            else:
                answer.append(getDivisors(n))
    
    return answer

def getDivisors(n):
    answer = set()
    for k in range(1, int(n**0.5)+1):
        if n%k == 0:
            answer.add(k)
            if n//k <= 10000000:
                answer.add(n//k)

    return max(answer)