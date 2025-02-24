def solution(arr1, arr2):
    # answer 행렬의 크기 지정 후 초기화
    a, b = len(arr1), len(arr2[0])
    answer = [[0 for _ in range(b)] for _ in range(a)]
    
    # 원소 하나씩 인덱스를 기준으로 arr1와 arr2로부터 계산한다.
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            answer[i][j] = mul(arr1[i], arr2, j)
    
    return answer

def mul(a1, a2, k):
    ans = 0
    a2 = [i[k] for i in a2]
    for i, j in enumerate(a1):
        ans += j*a2[i]
    return ans