def solution(s):
    answer = []
    # 길이 26의 -1 리스트를 생성하고 각 소문자가 어느 위치에 마지막으로 나왔는지 작성해둔다.
    record = [-1]*26
    
    for i, j in enumerate(s):
        loc = ord(j) - ord('a') # a = 0을 기준으로 한 인덱스 저장
        if record[loc] != -1:
            answer.append(i-record[loc])
        else:
            answer.append(-1)
        record[loc] = i # update
        
    return answer