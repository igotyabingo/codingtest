def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        target = array[a-1:b]
        target.sort()
        answer.append(target[c-1])
    
    return answer