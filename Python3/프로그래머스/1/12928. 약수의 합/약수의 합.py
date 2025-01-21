import math
def solution(n):
    if(n == 0): return 0
    sum = 0
    len = math.floor(math.sqrt(n))
    for i in range(1, len+1):
        if(n%i == 0):
            if(i != n//i):
                sum = sum + i + n//i
            else:
                sum += i
    return sum