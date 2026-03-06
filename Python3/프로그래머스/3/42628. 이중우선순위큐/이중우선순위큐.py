from heapq import heappush, heapify, heappop
from collections import deque, defaultdict

def solution(operations):
    # 최솟값, 최댓값을 모두 기록하고 있어야 함 -> minheap, maxheap 모두 두고 
    # dict으로 개수를 관리하고 있자 (판단 기준)
    maxheap, minheap = [], []
    heapify(maxheap) # -로 저장
    heapify(minheap) # 그대로 저장
    count = defaultdict(int)
    
    operations = deque(operations)
    
    while operations:
        command, num = operations.popleft().split()
        num = int(num)
        
        if command == 'I':
            heappush(maxheap, -num)
            heappush(minheap, num)
            count[num] += 1
        else:
            if num == 1: # 최댓값 삭제
                while maxheap and count[-maxheap[0]] == 0:
                    heappop(maxheap)
                if maxheap: 
                    k = -heappop(maxheap)
                    count[k] -= 1
            else: # 최솟값 삭제
                while minheap and count[minheap[0]] == 0:
                    heappop(minheap)
                if minheap:
                    k = heappop(minheap)
                    count[k] -= 1
    final_min_heap, final_max_heap = [], []
    heapify(final_max_heap)
    heapify(final_min_heap)
    
    for a in count:
        for _ in range(count[a]):
            heappush(final_max_heap, -a)
            heappush(final_min_heap, a)
    
    return [0, 0] if not final_max_heap else [-heappop(final_max_heap), heappop(final_min_heap)]
            