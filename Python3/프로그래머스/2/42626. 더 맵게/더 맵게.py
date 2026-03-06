from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    # using minheap -> heappush, heappop
    heapify(scoville) # 기본 = minheap
    
    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        a = heappop(scoville)
        b = heappop(scoville)
        
        heappush(scoville, a + b*2)
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return answer