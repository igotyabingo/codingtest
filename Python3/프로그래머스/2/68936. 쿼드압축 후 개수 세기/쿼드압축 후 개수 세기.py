def solution(arr):
    answer = [0, 0]

    l = len(arr)
    a = [[0 for _ in range(l)] for _ in range(l)]
    b = [[1 for _ in range(l)] for _ in range(l)]
    
    if arr == a: return [1, 0]
    elif arr == b: return [0, 1]

    queue = [arr]

    while queue:
        target = queue.pop(0)
        l = len(target)
        tmp = [[] for _ in range(4)]

        for i in range(l//2):
            tmp[0].append(target[i][:l//2])
            tmp[1].append(target[i][l//2:])
            tmp[2].append(target[i+l//2][:l//2])
            tmp[3].append(target[i+l//2][l//2:])

        a = [[0 for _ in range(l//2)] for _ in range(l//2)]
        b = [[1 for _ in range(l//2)] for _ in range(l//2)]
        

        for i in tmp:
            if i == a: answer[0] +=1
            elif i == b: answer[1] +=1
            else:
                queue.append(i)
            
    return answer