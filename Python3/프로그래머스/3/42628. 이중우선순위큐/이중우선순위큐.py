from heapq import heapify, heappop, heappush

def solution(operations):
    visited = set()
    minheap, maxheap = [], []
    
    for i, operation in enumerate(operations):
        if operation[0] == "I":
            num = int(operation[2:])
            heappush(minheap, (num, i))
            heappush(maxheap, (-num, i))
        else:
            if operation[2] == '-': # 최솟값 삭제
                while minheap:
                    x, idx = heappop(minheap)
                    if idx not in visited:
                        visited.add(idx)
                        break
            else: # 최댓값 삭제
                while maxheap:
                    x, idx = heappop(maxheap)
                    if idx not in visited:
                        visited.add(idx)
                        break
    max_value, min_value = 0, 0
    while maxheap:
        x, idx = heappop(maxheap)
        if idx not in visited:
            max_value = -x
            break
    while minheap:
        x, idx = heappop(minheap)
        if idx not in visited:
            min_value = x
            break
    
    return [max_value, min_value]