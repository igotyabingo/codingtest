def solution(citations):
    citations.sort(reverse=True)
    for i, val in enumerate(citations):
        if i+1 > val:
            return i
    return len(citations)