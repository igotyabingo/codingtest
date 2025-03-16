def solution(sequence, k):
    candidates = []
    partial_sum = 0
    
    tail = 0    
    for head in range(len(sequence)):
        for t in range(tail, len(sequence)):
            partial_sum += sequence[t]
            if (partial_sum >= k):
                if(partial_sum == k):
                    candidates.append((head, t))                
                break
        tail = t
        partial_sum -= sequence[head]+sequence[t]
    
    candidates.sort(key = lambda x: ((x[1]-x[0]), x[0]))
    return [candidates[0][0], candidates[0][1]]