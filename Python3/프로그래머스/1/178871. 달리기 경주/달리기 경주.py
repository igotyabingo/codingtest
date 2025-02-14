def solution(players, callings):
    
    # 시간복잡도를 위해 딕셔너리 구성
    dic = {}
    for i, j in enumerate(players):
        dic[j] = i
    
    for i in callings:
        k = dic[i]
        players[k-1], players[k] = players[k], players[k-1]
        dic[players[k-1]] = k-1
        dic[players[k]] = k
        
    return players