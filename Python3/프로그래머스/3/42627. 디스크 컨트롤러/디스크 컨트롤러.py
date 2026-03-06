import heapq
from collections import deque

def solution(jobs):
    l = len(jobs)
    answer = 0
    # jobs: [[0, 3], [1, 9], [3, 5]] -> i, 요청시각, 작업소요시간
    
    # 우선순위: 작업 소요시간 짧은 것 > 작업 요청시간 빠른 것 > 작업 번호가 작은 것
    # python에서 튜플 비교 = 앞에서부터 사전식으로 수행함
    # queue에 (작업 소요시간, 작업 요청시간, 작업 번호)로 heap 구성

    queue = []
    heapq.heapify(queue)
    time = 0 # 현재 시간 계산
    
    for i, job in enumerate(jobs):
        jobs[i] = (job[0], job[1], i)
    jobs.sort()
    
    jobs = deque(jobs)
    
    
    while queue or jobs: # 요청 시간, 작업 소요 시간
        while jobs and jobs[0][0] <= time:
            a, b, i = jobs.popleft()
            heapq.heappush(queue, (b, a, i))
        
        if not queue and jobs: 
            a, b, i = jobs.popleft()
            heapq.heappush(queue, (b, a, i))
        
        t2, t1, idx = heapq.heappop(queue)
        if time < t1:
            time = t1
        time += t2
        answer += (time-t1)
        
    return answer // l