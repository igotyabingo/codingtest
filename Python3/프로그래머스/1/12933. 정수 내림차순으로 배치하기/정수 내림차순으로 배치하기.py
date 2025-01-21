def solution(n):
    lst = [i for i in str(n)]
    lst.sort(reverse = True)
    return int(''.join(i for i in lst))