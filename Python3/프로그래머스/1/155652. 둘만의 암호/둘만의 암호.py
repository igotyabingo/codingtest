def solution(s, skip, index):
    answer = ''
    # 전체 소문자에서 skip 소문자들을 제외한 리스트를 구성한다.
    alp = sorted(list({chr(ord('a')+i) for i in range(26)}-set(skip)))
    
    s = list(s)
    for i in range(len(s)):
        s[i] = alp[(alp.index(s[i])+index)%len(alp)]
    
    return ''.join(i for i in s)