def solution(n,a,b):
    r = 1
    a, b = min(a,b), max(a,b)
    
    while(a%2 != 1 or b-a != 1):
        a, b = next_round(a), next_round(b)
        r += 1
    return r

def next_round(i):
    if(i%2 == 0):
        return i//2
    else:
        return (i+1)//2