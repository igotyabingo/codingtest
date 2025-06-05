
def solution(a):
    # 반드시 터지는 풍선의 특징이 있을 것이다 (인접한 원소들 관련)
    # 좌측 그룹 최솟값, 우측 그룹 최솟값 < 원소 이면 반드시 터진다
    answer = 0   
    n = len(a)
    left_min = [0]*n
    right_min = [0]*n
    left_min[0], right_min[n-1] = 1000000001,1000000001
    
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i-1])
    
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i+1])
        
    for i in range(n):
        if a[i] > left_min[i] and a[i] > right_min[i]:
            answer += 1
        
    return len(a)-answer