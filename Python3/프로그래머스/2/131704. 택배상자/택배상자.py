def solution(order):
    answer = 0
    stack = []  # 보조 컨테이너 벨트
    processing = 1

    for target in order:
    # 조건문을 깔끔하게 분기하자.
        if processing == target:
            processing += 1
            answer += 1
        elif (stack and stack[-1] == target):
            answer += 1
            stack.pop()
        # 위에서 target이 처리되는 경우를 모두 처리 함. 이 밑은 처리 못하는 경우
        elif (target > processing):
            while(target != processing):
                stack.append(processing)
                processing += 1
            answer += 1
            processing += 1
        else:
            break

    return answer