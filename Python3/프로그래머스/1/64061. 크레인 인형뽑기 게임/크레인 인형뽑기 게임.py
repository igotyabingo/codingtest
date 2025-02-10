def solution(board, moves):
    answer = 0
    l = len(board)
    stack = []  # 바구니를 스택으로 구현한다.
    
    # 1~ N번 세로줄을 모두 스택으로 구현한다.
    b = [[] for _ in range(l)]
    
    for i in range(l-1, -1, -1):
        a = board[i]
        for j in range(l-1, -1, -1):
            if a[j] != 0:
                b[j].append(a[j])
    
    for m in moves:
        if b[m-1]:
            k = b[m-1].pop()
            if stack and stack[-1] == k:
                stack.pop()
                answer += 2
            else:
                stack.append(k)
        
    return answer