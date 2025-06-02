import heapq

def solution(jobs):
    jobs.sort()
    minheap = []
    n = len(jobs)
    answer = 0 # 모든 소요시간 합
    count = 0

    while count < n:
        if not minheap: # 대기열이 비어있을 때 -> '점프'
            t = jobs[0][0] # t 시점으로 점프해서 t 시점에 들어오는 모든 job을 대기열에 저장한다.
            while jobs and jobs[0][0] == t:
                x, y = jobs.pop(0)
                heapq.heappush(minheap, (y, x))

        # 그럼 이제 대기열이 채워진다. 하나씩만 뺀다: 해당 작업을 시작한다.
        dt, start = heapq.heappop(minheap)
        t += dt # t초로부터 dt초 동안 작업을 수행한다.

        while jobs and jobs[0][0] <= t:
            x, y = jobs.pop(0)
            heapq.heappush(minheap, (y, x))

        # 현재 진행 중인 작업을 끝내고(answer 변수 업데이트), 다음 진행할 작업을 골라낸다.(t 업데이트)
        answer += (t-start)
        count += 1

    return answer//n