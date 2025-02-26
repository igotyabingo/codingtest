def solution(citations):
    citations.sort(reverse = True)
    
    for i in range(len(citations)-1, -1, -1):
        if(citations[i]>=i+1):
            break
            
    return i+1 if i>0 else 0