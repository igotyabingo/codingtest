# 모든 쌍에 대해 비교해야 함

def solution(friends, gifts):
    n = len(friends)
    
    # 사람 이름 - 인덱스 매핑할 딕셔너리 생성
    dic = {}
    for i, f in enumerate(friends):
        dic[f] = i
    
    # 선물 지수 리스트 초기화 (2차원 배열)
    gft = [[0]*n for _ in range(n)]
    for g in gifts:
        f1, f2 = g.split(' ')
        gft[dic[f1]][dic[f2]] += 1
        gft[dic[f2]][dic[f1]] -= 1
    
    # 두 사람 사이의 결과를 저장할 리스트 초기화
    result = []
    for i in range(n):
        for j in range(i+1, n):
            # 3가지 경우
            if(gft[i][j]>gft[j][i]):
                result.append(i)
            elif(gft[i][j]<gft[j][i]):
                result.append(j)
            else:
                # 선물 지수 비교
                if(sum(gft[i])>sum(gft[j])):
                    result.append(i)
                elif(sum(gft[i])<sum(gft[j])):
                    result.append(j)
                else:
                    result.append(-1)
    
    # 각 원소(사람 인덱스)의 최대 카운트값을 리턴한다.
    cnt = 0
    print(result)
    for i in range(n):
        cnt = max(cnt, result.count(i))
        
    return cnt
    