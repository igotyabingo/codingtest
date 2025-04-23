def solution(n, computers):
    answer = set()
    # union find 알고리즘
    roots = [i for i in range(n)]
    # 일단 처음은 각자 본인이 ROOT임

    for idx, values in enumerate(computers):
        for i in range(idx+1, n):
            if values[i] == 1:
                union(idx, i, roots)

    for r in roots:
        answer.add(find(r, roots))
    
    return len(answer)
     

def find(n, roots): 
    while roots[n] != n:
        n = roots[n]
    
    return n

def union(i, j, roots):
    roots_i, roots_j = find(i, roots), find(j, roots)
    if roots_i != roots_j:
        roots[roots_j] = roots_i