N = int(input())
channels = [input().strip() for _ in range(N)]

# 1. KBS1을 1번으로 만들기
# 2. KBS2를 2번으로 만들기 
# 를 순서대로 실행한다.
answer = ''

k = channels.index("KBS1")
channels.insert(0, channels.pop(k))
for _ in range(k):
    answer += '1'
for _ in range(k):
    answer += '4'

k = channels.index("KBS2")
for _ in range(k):
    answer += '1'
for _ in range(k-1):
    answer += '4'

print(answer)