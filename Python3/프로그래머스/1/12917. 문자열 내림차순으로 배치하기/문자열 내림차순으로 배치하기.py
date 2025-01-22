def solution(s):
    lst = [i for i in s]
    lst.sort(reverse=True)
    return ''.join(i for i in lst)