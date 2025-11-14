from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]

    t = 0 # 현재 시간
    queue = deque()
    
    for i, price in enumerate(prices):
        queue.append((i, price))
    
    # stack에 price 하나씩 push, top원소보다 더 작은 게 들어오면 pop
    stack = []
    # stack = [(t, price)]
    while queue:
        while stack and stack[-1][1] > queue[0][1]:
            time, _ = stack.pop()
            answer[time] = t-time
        stack.append(queue.popleft())
        t += 1
        
    while stack:
        time, _ = stack.pop()
        answer[time] = t-time-1
        
    return answer