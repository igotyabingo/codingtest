import heapq

def solution(operations):
    idx = 0
    maxheap = []
    minheap = []
    dic = []

    for o in operations:
        if o[0] == 'I':
            num = int(o[2:])
            heapq.heappush(minheap, (num, idx))
            heapq.heappush(maxheap, (-num, idx))
            idx += 1
            dic.append(True)
        else:
            if o[2] == '-':
                while minheap and not dic[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    _, x = heapq.heappop(minheap)
                    dic[x] = False
            else:
                while maxheap and not dic[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    _, x = heapq.heappop(maxheap)
                    dic[x] = False

    while minheap and dic[minheap[0][1]]==False:
        heapq.heappop(minheap)
    if minheap: 
        min = minheap[0][0]
    else:
        return [0, 0]
    
    while maxheap and dic[maxheap[0][1]]==False:
        heapq.heappop(maxheap)
    if maxheap:
        max = -maxheap[0][0]
    
    return [max, min]