from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while(scoville[0] < K):
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a+2*b)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K: return -1
    
    return answer