def solution(prices):
    answer = [-1 for _ in range(len(prices))]
    stack = []
    
    for i, j in enumerate(prices):
        while(stack and stack[-1][1]>j):
            p, q = stack.pop()
            answer[p] = i-p
        stack.append((i, j))
    
    for s in stack:
        p, _ = s
        answer[p] = i-p
        
    return answer