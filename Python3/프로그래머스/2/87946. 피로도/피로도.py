from itertools import permutations

def solution(k, dungeons):
    perm = list(permutations([i for i in range(len(dungeons))]))
    cand = []
    
    for p in perm:  # 가능한 모든 순서를 탐색한다.
        c, temp = 0, k
        for i in p:
            if(temp>=dungeons[i][0]):
                temp -= dungeons[i][1]
                c += 1
            else:
                break
        cand.append(c)

    return(max(cand))