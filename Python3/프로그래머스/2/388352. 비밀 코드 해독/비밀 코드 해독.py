from itertools import combinations

def solution(n, q, ans):
    answer = 0
    # n, m의 크기 제한이 크지 않아 모든 조합을 확인해보는 게 오히려 더 빠를 수도 있다.
    # 최선: 가장 많이 일치하는 조합으로부터 후보 생성한다
    k = max(ans)
    m = q[ans.index(k)]
    
    if(k==5):
        return 1
    elif(k==4):
        for i in range(5):
            new_set = set(m[:i] + m[i+1:])
            for j in [p for p in range(1, n+1) if p not in m]:
                answer += 1 
                for a, b in enumerate(q):
                    if not (check(new_set|{j}, b, ans[a])):
                        answer -= 1
                        break
                
    elif(k==3):
        cand = list(combinations(m, 3))
        for i in cand:
            for j in list(combinations([p for p in range(1, n+1) if p not in m], 2)):
                answer += 1
                for a, b in enumerate(q):
                    if not (check(set(i)|set(j), b, ans[a])):
                        answer -= 1 
                        break
                
        
    elif(k==2):
        cand = list(combinations(m, 2))
        for i in cand:
            for j in list(combinations([p for p in range(1, n+1) if p not in m], 3)):
                answer += 1
                for a, b in enumerate(q):
                    if not (check(set(i)|set(j), b, ans[a])):
                        answer -= 1 
                        break
                
    else:
        for i in range(5):
            new_set = {m[i]}
            for j in list(combinations([p for p in range(1, n+1) if p not in m], 4)):
                answer += 1
                for a, b in enumerate(q):
                    if not (check(new_set|set(j), b, ans[a])):
                        answer -= 1
                        break
    return answer

def check(set1, list2, count):
    # set1과 list2의 일치하는 개수가 count개인지 확인한다.
    return len(set1&set(list2))==count