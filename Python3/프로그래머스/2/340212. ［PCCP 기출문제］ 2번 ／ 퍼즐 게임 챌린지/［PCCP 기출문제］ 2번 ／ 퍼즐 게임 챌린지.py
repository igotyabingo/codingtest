def solution(diffs, times, limit):
    # level은 1부터 max(diffs) 까지의 값을 가질 수 있다. 
    # 해당 범위의 모든 정수를 배열 값으로 가지는 배열을 이진 탐색한다.
    low, high = 1, max(diffs)
    answer = high
    
    while(low <= high):
        mid = (low+high) // 2
        if calculate(diffs, times, mid) <= limit:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return answer

def calculate(diffs, times, level):
    tmp, prev = 0, 0
    time_sum = 0
    
    for i in range(len(diffs)):
        time_sum += (prev+times[i])*(max(0, diffs[i]-level))+times[i]
        prev = times[i]
    
    return time_sum