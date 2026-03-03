def solution(genres, plays):
    answer = []
    # 1. 장르 정렬: 장르에 속한 노래들의 전체 재생 횟수가 많은 순서대로
    # 2. 장르 내 노래 정렬: 각 노래의 재생 횟수가 많은 순서대로
    # -> 재생횟수가 동일할 경우, 고유 번호 순서대로
    
    # 1. 장르별 총 재생횟수 구하기
    # 2. 장르별 노래 번호, 재생횟수 정리하기
    
    lst = dict()
    # genre = [총 재생횟수, [[노래번호, 재생횟수], [노래번호, 재생횟수], ... ]]
    for i in range(len(genres)):
        if genres[i] not in lst:
            lst[genres[i]] = [0, []]
        lst[genres[i]][0] += plays[i]
        lst[genres[i]][1].append([i, plays[i]])
    
    for g in sorted(lst, key = lambda x:lst[x][0], reverse=True):
        target = sorted(lst[g][1], key=(lambda x:x[1]), reverse=True)
        for element in target[:2]:
            answer.append(element[0])
        
    return answer