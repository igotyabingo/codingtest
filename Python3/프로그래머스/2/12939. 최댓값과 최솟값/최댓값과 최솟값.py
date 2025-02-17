def solution(s):
    lst = [int(i) for i in s.split()]
    # map 함수를 응용해볼 수 있다: s.split()에 int함수를 매핑
    # list = list(map(int, s.split()))
    
    return f'{min(lst)} {max(lst)}'
