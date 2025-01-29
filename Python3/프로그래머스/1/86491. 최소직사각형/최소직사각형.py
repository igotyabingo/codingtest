def solution(sizes):
    lst1 = []
    lst2 = []
    
    for s in sizes:
        lst1.append(max(s))
        lst2.append(min(s))
        
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)
    
    return lst1[0]*lst2[0]