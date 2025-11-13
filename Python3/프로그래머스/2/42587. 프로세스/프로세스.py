from collections import defaultdict, deque

def solution(priorities, location):
    # 우선순위 별 process 개수 저장
    p = defaultdict(int)
    queue = []
    
    for i, pr in enumerate(priorities):
        p[pr] += 1
        queue.append((i, pr))
        
    queue = deque(queue)
    mx = max(p)
    rank = 1
    
    while queue:
        x, y = queue.popleft()
        if y < mx:
            queue.append((x, y))
        else: # y = mx
            if location == x:
                return rank
            p[mx] -= 1
            if p[mx] == 0:
                del p[mx]
                mx = max(p)
            rank += 1
