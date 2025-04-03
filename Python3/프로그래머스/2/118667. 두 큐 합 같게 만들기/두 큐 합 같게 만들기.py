# list.pop(0) = O(N), deque.popleft() = O(1)
from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    limit = len(queue1)*3
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count = 0

    while(sum1 != sum2):
        if count > limit: return -1
        count += 1
        if sum1 > sum2:
            # queue1에서 queue2로 원소를 하나 옮긴다.
            target = queue1.popleft()
            queue2.append(target)
            sum1 -= target
            sum2 += target
        else:
            # queue2에서 queue1로 원소를 하나 옮긴다.
            target = queue2.popleft()
            queue1.append(target)
            sum2 -= target
            sum1 += target

    return count