def solution(citations):
    citations.sort(reverse=True)
    h = 0
    
    for i, val in enumerate(citations):
        h = max(h, min(i+1, val))
    
    return h
