def solution(info, n, m):
    # i번째 round에서 생성하는 temp 배열의 원소: i번째 물건을 훔쳤을 때 (A의 흔적 개수, B의 흔적 개수)

    tmp = set([(0, 0)])
    for i in range(len(info)):
        # 물건 하나씩
        temp = set()
        if not tmp:
            return -1

        for t in tmp:
            x, y = t
            # 1. 이번 물건을 B가 훔치게 한다.
            if y+info[i][1] < m:
                temp.add((x, y+info[i][1]))

            # 2. 이번 물건을 A가 훔치게 한다.
            if x+info[i][0] < n:
                temp.add((x+info[i][0], y))

        tmp = temp 
        
    return -1 if not tmp else min([i[0] for i in tmp])