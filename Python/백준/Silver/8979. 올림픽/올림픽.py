N, K = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

countries.sort(reverse = True, key = lambda x: x[3])
countries.sort(reverse = True, key = lambda x: x[2])
countries.sort(reverse = True, key = lambda x: x[1])

check = set()
rank = 0 # 바로 다음으로 지정할 순위
people = 1

for idx, x, y, z in countries: 
    if (x, y, z) not in check: 
        rank += people
        check.add((x, y, z))
        people = 1
    else:
        # rank 그대로
        people += 1

    if idx == K:
        print(rank)

# 공동 등수를 어떻게 처리 할 것인가: 하나 추가할때마다 set 크기를 확인한다?