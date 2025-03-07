def solution(numbers):
    stack = []
    answer = [-1 for _ in range(len(numbers))]
    
    for i, j in enumerate(numbers):
        while(stack and j > stack[-1][1]):
            k = stack.pop()
            answer[k[0]] = j
            
        stack.append((i, j))
    return answer