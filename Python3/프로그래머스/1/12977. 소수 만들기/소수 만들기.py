def solution(nums):
    answer = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if(check(nums[i]+nums[j]+nums[k])):
                    answer += 1
    return answer

# 소수인지 확인할 수 있는 함수를 작성한다
def check(n):
    # 짝수면 바로 false를 리턴
    if (n%2==0):
        return False
    else:
        # 홀수인 경우, root n보다 작은 홀수로 모두 나눠본다
        for i in range(3, int(n**(1/2))+1, 2):
            if(n%i == 0):
                return False
        return True
        
        