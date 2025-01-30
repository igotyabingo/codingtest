def solution(array, commands):
    answer = []
    
    for a, b, c in commands:
        lst = array[a-1:b]
        lst.sort()
        answer.append(lst[c-1])
        
    return answer