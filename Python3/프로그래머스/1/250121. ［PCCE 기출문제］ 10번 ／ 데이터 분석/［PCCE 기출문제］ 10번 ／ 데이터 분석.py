def solution(data, ext, val_ext, sort_by):
    answer = []
    # WHERE문 적용컬럼: ext
    # WHERE문 기준값: val_ext
    # ORDER BY 기준컬럼: sort_by
    # SELECT * WHERE ext < val_ext ORDER BY sort_by ASC;
    
    dic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    # 1. answer 배열에 WHERE문을 만족시키는 것들을 모두 넣는다.
    for i in data:
        if(i[dic[ext]] < val_ext):
            answer.append(i)
    
    # 2. answer 배열을 sort_by 기준으로 소팅하고 리턴한다.
    return sorted(answer, key = lambda x: x[dic[sort_by]])
