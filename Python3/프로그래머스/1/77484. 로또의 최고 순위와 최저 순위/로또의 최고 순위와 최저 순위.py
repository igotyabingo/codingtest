def solution(lottos, win_nums):
    
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    n = len(set(lottos)&set(win_nums))
    m = lottos.count(0)
    m = min(6, m+n)
    
    return [dic[m], dic[n]]