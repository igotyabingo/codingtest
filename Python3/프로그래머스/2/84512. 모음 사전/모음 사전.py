def solution(word):
    answer = 0
    
    x = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    y = {0: 781, 1: 156, 2: 31, 3: 6, 4: 1}
    
    for i, j in enumerate(word):
        answer += y[i]*x[j]+1
    
    return answer