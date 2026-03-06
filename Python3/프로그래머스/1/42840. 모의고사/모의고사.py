def solution(answers):
    rank = []
    # 패턴
    # 1번: 5개 주기
    # 2번: 8개 주기
    # 3번: 10개 주기
    score1, score2, score3 = 0, 0, 0
    a1 = [1, 2, 3, 4, 5] * 2000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    for i, answer in enumerate(answers):
        if answer == a1[i]: score1 += 1
        if answer == a2[i]: score2 += 1
        if answer == a3[i]: score3 += 1
    
    scores = [[score1, 1], [score2, 2], [score3, 3]]
    scores = sorted(scores, key=lambda x: (-x[0], x[1]))
    
    rank.append(scores[0][1])
    
    if scores[1][0] == scores[0][0]:
        rank.append(scores[1][1])
        if scores[2][0] == scores[1][0]:
            rank.append(scores[2][1])
    
    return rank
    