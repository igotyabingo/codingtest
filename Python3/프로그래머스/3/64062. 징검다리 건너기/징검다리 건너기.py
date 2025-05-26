# 이분 탐색을 이용한다.
def solution(stones, k):
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        # '연속된' 초과구간을 찾는다. 길이가 k '이상'이면 안된다.
        count = 0
        for stone in stones:
            if stone <= mid: 
                count += 1
                if count >= k:
                    break
            else:
                count = 0
        
        if count >= k:
            right = mid-1
        else:
            left = mid+1
    
    return left