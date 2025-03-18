def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: x[0], reverse = True)
    data.sort(key = lambda x: x[col-1])

    for i in range(row_begin-1, row_end):
        answer ^= sum([d%(i+1) for d in data[i]])
        
    return answer