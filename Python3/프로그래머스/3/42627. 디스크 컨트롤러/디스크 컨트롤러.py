from heapq import heappush, heappop, heapify
from collections import deque

def solution(jobs):
    time = 0 
    n = len(jobs)
    # heapq = 대기 큐 => (작업 소요시간, 작업 요청시각, 작업 번호)로 저장 후 우선순위 비교
    lst = []
    
    job_list = deque()
    jobs.sort(key=lambda x: x[0])
    for i, job in enumerate(jobs):
        job_list.append((job[1], job[0], i))

    t = 0
    while job_list or lst: # 초 단위로 수행
        # 1. 대기 큐에 삽입
        while job_list and job_list[0][1] <= t:
            heappush(lst, job_list.popleft())
        
        # 2. 하나 뽑기
        if lst: 
            x, y, z = heappop(lst)
            t += x
            time += (t-y)
        else:
            t += 1
    
    return time // n