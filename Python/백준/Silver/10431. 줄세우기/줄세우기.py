P = int(input())
# 항상 정렬된 상태임 -> stack

for _ in range(P):
    cm = [int(i) for i in input().split()] # 한 줄씩 입력을 받음
    count = 0
    stack = [cm[1]]

    for k in cm[2:]:
        if k > stack[-1]:
            stack.append(k)
        else:
            # 자기 자리를 찾아야 하고, count를 증가시켜야 한다.
            i = len(stack)-1
            while stack[i] > k and i > -1:
                i -= 1
                count += 1
            stack.insert(i+1, k)

    print(cm[0], count)