p, m = map(int, input().split())
rooms = []
finished = set()
scope = [[] for _ in range(501)]

# 방 저장: 생성 순서(인덱스), (레벨, 정원, [플레이어])
for _ in range(p):
    l, n = input().split()
    l = int(l)

    # 새로운 방 생성하는 경우인지 확인
    create = True
    target = False

    for k in scope[l]:
        if k not in finished:
            target = k # k번째 방에 들어가면 된다.
            create = False
            break

    # 1. 새로운 방 생성하는 경우
    if create:
        rooms.append([l, 1, [(l, n)]])
        idx = len(rooms)-1
        if m == 1:
            finished.add(idx)
        else:
            for k in range(l-10, l+11):
                if 0 <= k <= 500:
                    scope[k].append(idx)
    else:
        # 2. 기존 방 들어가는 경우
        rooms[target][1] += 1
        if rooms[target][1] == m:
            finished.add(target)
        rooms[target][2].append((l, n))

for room in rooms:
    if room[1] == m:
        print("Started!")
    else: 
        print("Waiting!")

    for l, n in sorted(room[2], key = lambda x: x[1]) :
        print(l, n)