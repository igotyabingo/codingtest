def solution(n, m, section):
    answer = 0
    pos = section[0]
    
    for i in section[1:]:
        if(pos+m <= i):
            # update
            pos = i
            answer += 1
            
    return answer+1

# 처음에는 set의 차집합 연산을 이용하여 풀었으나 len(section)**2의 시간이 소요되면 몇가지 테케에서 시간이 초과됨
