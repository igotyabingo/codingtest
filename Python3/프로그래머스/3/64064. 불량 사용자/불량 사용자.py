from collections import defaultdict

def solution(user_id, banned_id):
    # 1. id 길이 별로 dictionary 를 구성한다.
    dic = defaultdict(list)
    for id in user_id:
        dic[len(id)].append(id)

    queue = []

    # 2. 각 banned_id 원소에 대해 후보군을 찾는다.
    for x, id in enumerate(banned_id):
        l = len(id)
        tmp = []
        for cand in dic[l]:
            value = True
            for i in range(l):
                if id[i]!='*' and id[i]!=cand[i]:
                    value = False
                    break
            if value:
                if x == 0:
                    queue.append([cand])
                else:
                    for q in queue:
                        if cand not in q:
                            tmp.append(q+[cand])
        if x!= 0: queue = tmp
    
    return len(set([tuple(sorted(i)) for i in queue]))