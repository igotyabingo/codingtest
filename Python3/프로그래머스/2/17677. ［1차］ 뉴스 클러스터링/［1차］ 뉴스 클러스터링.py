import re

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 딕셔너리 카운터를 구성한다.
    set1, set2 = dict(), dict()
    
    for i in range(len(str1)-1):
        target = str1[i:i+2]
        if not (re.search(r'[^a-z]', target)):  # 알파벳이 아닌 게 포함된 것을 제외한다.
            if target in set1:
                set1[target] += 1
            else:
                set1[target] = 1
        
    for i in range(len(str2)-1):
        target = str2[i:i+2]
        if not (re.search(r'[^a-z]', target)):
            if target in set2:
                set2[target] += 1
            else:
                set2[target] = 1
            
    if not (set1 or set2):
        return 65536
    
    hap, gyo = set1.copy(), dict()
    for i in set2:
        if i in hap:
            hap[i] = max(hap[i], set2[i]) 
        else:
            hap[i] = set2[i]

    for i in set1:
        if i in set2:
            gyo[i] = min(set1[i], set2[i])
    
    return int((sum(gyo.values())/sum(hap.values()))*65536)