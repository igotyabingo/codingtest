def solution(s):
    s = s.lower()   # 모두 소문자로 통일시킴
    return True if s.count('p')==s.count('y') else False