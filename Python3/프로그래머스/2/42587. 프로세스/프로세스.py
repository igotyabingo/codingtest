from collections import deque

def solution(priorities, location):
    answer = 0
    # priorities[location] process의 실행 순서 찾기
    
    # queue 순서대로 확인. "우선순위가 가장 높은 경우" 실행
    # 그렇지 않을 경우 맨 뒤에 다시 삽입함
    
    ranks = deque(sorted(priorities, reverse=True))
    
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i, p)) # (index, priority)
    
    rank = 1
    while queue:
        if ranks[0] == queue[0][1]:
            if queue[0][0] == location:
                return rank
            ranks.popleft()
            queue.popleft()
            rank += 1
        else:
            queue.append(queue.popleft())
