H, W, N, M = map(int, input().split())

a, b = 0, 0
for i in range(1, H+1, N+1):
    a += 1

for i in range(1, W+1, M+1):
    b += 1

print(a*b)