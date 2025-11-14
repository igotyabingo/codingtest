from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0 
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        x, y = heappop(scoville), heappop(scoville)
        heappush(scoville, x+2*y)
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer