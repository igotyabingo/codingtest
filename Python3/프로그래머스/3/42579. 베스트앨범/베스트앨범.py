def solution(genres, plays):
    answer = []
    dic = dict()
    # key: 장르명, value: [총재생수, [(고유번호, 재생수)]]

    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append((i, plays[i]))
        else:
            dic[genres[i]] = [plays[i], [(i, plays[i])]]

    genre_rank = sorted(dic, reverse=True, key=lambda x: dic[x][0])

    for genre in genre_rank:
        dic[genre][1].sort(key=lambda x: x[0])
        dic[genre][1].sort(reverse=True, key=lambda x: x[1])

        for value in dic[genre][1][:2]:
            answer.append(value[0])
    
    return answer