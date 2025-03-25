def solution(numbers):
    answer = []
    for n in numbers:
        if bin(n)[-2:] != '11':
            answer.append(n+1)
        else:
            tmp = bin(n)[2:][::-1]
            k = len(tmp)
            for i, j in enumerate(tmp):
                if j == '0': 
                    k = i
                    break
            answer.append(n+2**(k-1))
    return answer