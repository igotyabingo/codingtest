from collections import deque

def solution(prices):
    # ****
    answer = [0 for _ in range(len(prices))]
    queue = deque()
    stack = []
    
    for i, price in enumerate(prices):
        queue.append((i, price))
    
    t = 0
    while queue:
        while stack and stack[-1][1] > queue[0][1]: # 가격이 떨어짐
            time, _ = stack.pop()
            answer[time] = t - time
        stack.append(queue.popleft())
        t += 1
    
    for a, b in stack:
        answer[a] = t - a - 1
    return answer