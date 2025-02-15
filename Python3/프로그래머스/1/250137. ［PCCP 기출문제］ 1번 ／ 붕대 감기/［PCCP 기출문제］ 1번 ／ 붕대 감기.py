# 더했을 때 최대 체력을 넘으면 회복을 아예 안하는 게 아니라 최대 체력만큼은 회복하고 넘어간다.
# 최대 체력일 때도 연속 성공으로 더한다.

def solution(bandage, health, attacks):
    answer = health # 현재 체력을 저장할 변수
    con = 0 # 연속 성공 초를 저장할 변수
    t, x, y = bandage
    
    attack = {}
    for a, b in attacks:
        attack[a] = b
        
    # 마지막 공격까지 1초 지날때마다 동일한 조건들을 확인하면서 반복해야 함.
    for i in range(attacks[-1][0]+1):
        # 1. 몬스터의 공격이 들어왔는가?
        if i in attack:
            con = 0
            answer -= attack[i]
            if (answer <= 0):
                return -1
            
        else:
            con += 1
            if (con == t):
                con = 0
                answer = min(answer+x+y, health)
            else:
                answer = min(answer+x, health)
    return answer
