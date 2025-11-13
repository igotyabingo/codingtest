def solution(genres, plays):
    answer = []
    
    count = dict()
    # count[classic] = {count합, [(수록곡, count)]}
    # 1. count합 기준으로 장르 정렬
    # 2. 수록곡 list 정렬
    
    for i, genre in enumerate(genres):
        if genre not in count:
            count[genre] = [0, []]
        count[genre][0] += plays[i]
        count[genre][1].append((i, plays[i]))
    
    count = dict(sorted(count.items(), key=lambda x:x[1][0], reverse=True))
    for lst in count.values():
        pieces = sorted(lst[1], key=lambda x:(x[1], -x[0]), reverse=True)
        for piece in pieces[:2]:
            answer.append(piece[0])
            
    return answer