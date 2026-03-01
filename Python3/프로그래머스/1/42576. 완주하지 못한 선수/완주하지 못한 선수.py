from collections import Counter
def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    
    for name in p:
        if not c[name] or p[name]!=c[name]:
            return name