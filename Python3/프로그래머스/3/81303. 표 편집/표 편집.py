def solution(n, k, cmd):
    answer = ''
    # 꼬리 잡기로 생각한다. = linked list
    up = [i-1 for i in range(n)]
    down = [i+1 for i in range(n)]
    stack = [] # (지운 행, 기존up, 기존down)
    head, tail = 0, n-1
    up[head], down[tail] = tail, head

    for command in cmd:
        if command[0] == 'U':
            i = int(command[2:])
            for _ in range(i):
                k = up[k]
        elif command[0] == 'D':
            i = int(command[2:])
            for _ in range(i):
                k = down[k]
                
        elif command[0] == 'C':
            a, b = up[k], down[k]
            down[a], up[b] = b, a
            up[k], down[k] = n+2, n+2
            stack.append((k, a, b))
            
            if k == tail:     
                tail = a
                k = tail
            elif k == head:
                head = b
                k = b
            else: # 기본
                k = b
        else:
            z, x, y = stack.pop()
            
            down[x] = z
            up[y] = z
            up[z], down[z] = x, y
            if z > tail:
                tail = z
            elif z < head:
                head = z
                
                
    for i in range(n):
        if up[i] != n+2:
            answer += 'O'
        else: answer += 'X'
            
    return answer