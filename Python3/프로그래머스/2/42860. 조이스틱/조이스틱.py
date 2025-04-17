def solution(name):
    updown = 0

    # 위 아래 방향
    for alp in name:
        updown += min(ord(alp) - ord('A'), ord('Z')-ord(alp)+1)

    count = len(name) - name.count('A') # A가 아닌(조작해야 하는) 문자의 개수
    if count == 0:
        return 0
    queue = []

    # index 0 확인
    if name[0] == 'A':
        queue.append((1, 0, name, 1, True))
        queue.append((len(name)-1, 0, name, 1, False))
    else:
        queue.append((1, 1, 'A'+name[1:], 1, True))
        queue.append((len(name)-1, 1, 'A'+name[1:], 1, False))
    
    while(queue):
        x, y, target, value, direction = queue.pop(0)
        right = (x + 1) % len(name)
        left = (x - 1 + len(name)) % len(name)

        if direction: # 증가 방향
            if target[x] == 'A':
                queue.append((right, y, target, value+1, True))
                queue.append((left, y, target, value+1, False))
            else:
                if y+1 == count:
                    return updown + value
                queue.append((right, y+1, target[:x]+'A'+target[x+1:], value+1, True))
                queue.append((left, y+1, target[:x]+'A'+target[x+1:], value+1, False))

        else: # 감소 방향
            if target[x] == 'A':
                queue.append((left, y, target, value+1, False))
                queue.append((right, y, target, value+1, True))
            else:
                if y+1 == count:
                    return updown + value
                queue.append((left, y+1, target[:x]+'A'+target[x+1:], value+1, False))
                queue.append((right, y+1, target[:x]+'A'+target[x+1:], value+1, True))
        