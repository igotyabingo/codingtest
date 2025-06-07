# 모든 정점 간의 관계를 파악하기 위해 floyd-warshall 알고리즘을 사용한다.
def solution(n, results):
    answer = 0
    result = [[0]*(n+1) for _ in range(n+1)]
    
    for a, b in results:
        result[a][b] = 1    # a > b
        result[b][a] = -1   # b < a
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1
                    result[j][i] = -1
                elif result[i][k] == -1 and result[k][j] == -1:
                    result[i][j] = -1
                    result[j][i] = 1
    
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if result[i][j] != 0:
                count += 1
        
        if count == n-1:
            answer += 1
                    
    return answer