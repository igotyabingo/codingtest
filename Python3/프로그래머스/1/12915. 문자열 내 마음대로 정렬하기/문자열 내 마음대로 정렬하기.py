def solution(strings, n):
    answer = []
    
    ind = {word: word[n] for word in strings}
    # value: x[1] 기준으로 정렬한 후 (n번째 인덱스의 문자), 같으면 key: x[0] 기준으로 정렬
    sorted_ind = sorted(ind.items(), key=lambda x: (x[1], x[0]))
    
    for k, _ in sorted_ind:
        answer.append(k)
    
    return answer