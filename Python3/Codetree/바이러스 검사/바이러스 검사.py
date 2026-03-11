# n개의 식당에 있는 '고객들'의 체온 측정
# 체온 측정하는 '검사자' = '검사팀장' + '검사팀원'

# 식당 하나 당 한 팀 배정, 팀장 1명 + 팀원 0명 이상
# n개의 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수의 최솟값

# 각 식당 별로 팀장 한명 무조건, 팀원 수만 추가적으로 고려하면 됨
import math

def main():
    n = int(input())
    answer = n # 기본적으로 팀장 n명이 필요함. 추가로 필요한 팀원들의 수만 해당 변수에 더하여 출력
    customers = list(map(int, input().split()))
    head, manager = map(int, input().split())
    
    for num in customers:
        if num > head: # 반대의 경우에는 고려할 필요가 없음
            answer += math.ceil((num-head)/manager)
    
    print(answer)

if __name__ == "__main__":
    main()