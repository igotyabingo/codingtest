from heapq import heappop, heapify, heappush

def solution(sizes):
    # WLOG 가로 > 세로 고정
    width, height = [], []
    heapify(width)
    heapify(height)
    
    for w, h in sizes: 
        heappush(width, -max(w, h))
        heappush(height, -min(w, h))
        
    return (heappop(width)*heappop(height))
        
        