def solution(numbers):
    answer = ''
    zero = 0 # 0의 개수: 0은 마지막에 붙인다
    
    for i, j in enumerate(numbers):
        numbers[i] = str(j)
    
    # bucket sort / hash 의 형태를 사용한다
    bucket = dict()
    for i in range(9):
        bucket[str(i+1)] = []
    
    for i in numbers:
        if(i == '0'):
            zero += 1
        else:
            bucket[i[0]].append(i)
    
    for i in range(9, 0, -1):
        bucket[str(i)].sort(reverse=True, key=lambda x: x*3)
        answer += ''.join(bucket[str(i)])
    
    return answer+'0'*zero if answer else '0'