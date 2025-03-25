from heapq import heappop, heappush

def solution(n, k, enemy):
    max_heap = []
    sum = 0
    
    for i, j in enumerate(enemy):
        if sum + j > n:
            if k == 0: return i
            else:
                if max_heap and max_heap[0]<-j: 
                    sum = sum + heappop(max_heap) + j
                    heappush(max_heap, -j)
                k -= 1
        else:
            sum += j
            heappush(max_heap, -j)
    
    return len(enemy)