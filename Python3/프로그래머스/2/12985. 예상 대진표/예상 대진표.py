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

'''
while a != b:
    answer += 1
    a, b = (a+1)//2, (b+1)//2    
와 같이 작성하면 1,2 vs 2,3 처리도 되고 짝수 홀수 나눠서 다음 라운드 번호를 구핦 필요도 없다.
'''
