from collections import deque
import math

def solution(progresses, speeds):
    # queue 자료구조 이용
    # 각 작업: 몇일 후에 배포 가능한 지부터 계산
    # 앞의 원소 >= 뒤의 원소 일 경우 한꺼번에 나감, 아니면 따로
    
    answer = []
    
    n = len(progresses)
    days = []
    
    for i in range(n):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    days = deque(days)
    day, k = days.popleft(), 1
    while days:
        if day >= days[0]:
            days.popleft()
            k += 1
        else:
            answer.append(k)
            day, k = days.popleft(), 1
            
    answer.append(k)
    return answer