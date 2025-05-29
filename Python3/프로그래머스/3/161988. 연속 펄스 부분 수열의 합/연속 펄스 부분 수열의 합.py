# bottom up DP를 사용한다. 마지막 원소부터 (해당 원소를 시작점으로 지정했을 경우의) 값들을 저장한다.
def solution(sequence):
    n = len(sequence)
    value = [] 
    # value[i][0] = sequence[i]에서 +1로 시작했을 때 최대 합, value[i][1] = sequence[i]에서 -1로 시작했을 때 최대 합
    value = [[0, 0] for _ in range(n+1)]
    answer = 0

    for i in range(n-1, -1, -1):
        value[i][0] = max(value[i+1][1]+sequence[i], sequence[i])
        value[i][1] = max(value[i+1][0]-sequence[i], -sequence[i])
        answer = max(answer, value[i][0], value[i][1])
    
    return answer