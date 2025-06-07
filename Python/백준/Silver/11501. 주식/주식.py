T = int(input())

for _ in range(T):
    n = input()
    lst = [int(i) for i in input().split()]

    answer = 0 
    max_value = lst[-1]

    for i in range(len(lst)-1, -1, -1):
        if lst[i] >= max_value:
            # 안 사고 안 판다.
            max_value = lst[i] 
        else:
            answer += (max_value - lst[i])
    print(answer)