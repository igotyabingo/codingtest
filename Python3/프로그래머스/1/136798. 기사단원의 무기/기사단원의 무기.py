def solution(number, limit, power):
    answer = 0
    # 자신의 기사 번호의 약수개수에 해당하는 공격력 > 제한 수치: 정해진 수치의 공격력
    
    for i in range(1, number+1):
        a = div(i)
        if a > limit:
            answer += power
        else:
            answer += a
    return answer

# 약수 개수를 구하는 함수를 만든다. 
def div(n):
    ans = 0
    for i in range(1, n+1):
        if(n < i**2):
            break
        if(n == i**2):
            ans += 1
        elif(n%i == 0):
            ans += 2
            
    return ans
    