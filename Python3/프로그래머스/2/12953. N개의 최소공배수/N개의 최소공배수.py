def solution(arr):
    answer = 1
    # arr의 각 원소의 범위와 arr의 길이가 크지 않으므로 약수 set을 구성한다.
    div = set()
    for i in arr:
        div = div|divide(i) # 모든 수의 약수를 한 세트에 담음.
        div.remove(1)
    for i in div:
        # val이 False가 될때 까지 반복해서 i로 나눔
        k = divide_arr(arr, i)
        arr, val = k[:-1], k[-1]
        while(val):
          answer *= i
          k = divide_arr(arr, i)
          arr, val = k[:-1], k[-1]
    
    return answer*mul_list(arr)

def divide(i):  # i의 약수를 전부 구하는 함수
    ans = set()
    for j in range(1, int(i**(1/2))+1):
        if(i%j == 0):
            ans = ans|{j, i//j}
    return ans

def divide_arr(arr, n):
    val = False
    for i, j in enumerate(arr):
        if(j%n == 0):
            arr[i] = j//n
            val = True
    return arr + [val]

def mul_list(list):
    ans = 1
    for i in list:
        ans*=i
    return ans