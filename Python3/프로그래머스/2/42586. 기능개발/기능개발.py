from collections import deque
import math

def solution(progresses, speeds):
    # use queue. 반드시 처음 들어온 원소가 먼저 나갈 수 있다.
    answer = []
    
    # 미리 필요한 일수를 계산해둔다.
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    # 기준과 첫번째 원소를 비교한다.
    target, count = days.popleft(), 1
    while days:
        if target >= days[0]:
            count += 1
            days.popleft()
        else:
            answer.append(count)
            target = days.popleft() # 새로운 기준이 된다.
            count = 1
        
    return answer + [count]