def solution(array, commands):
    answer = []
    
    for a, b, x in commands:
        lst = sorted(array[a-1:b])
        answer.append(lst[x-1])
    return answer