from itertools import combinations
def solution(relation):
    answer = 0
    k = len(relation[0])
    count = len(relation)
    candidates = [i for i in range(k)]
    num = 1
    passed = []
    
    while num <= k:
        lst = list(combinations(candidates, num))

        for l in lst:
            s = set()
            for r in relation:
                tmp = ' '.join(str(r[p]) for p in l)
                s.add(tmp)

            if len(s) == count:
                temp = ''.join(str(i) for i in l)
                bool = True
                for p in passed:
                    if all(c in temp for c in p):
                        bool = False
                        break
                if bool:
                    answer += 1
                    passed.append(temp)
        num += 1

    return answer