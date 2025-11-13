def solution(arr):
    answer = []
    # 바로 앞 원소(스택의 top = answer[-1])와 같으면 정답 배열에 추가하지 않음
    for a in arr:
        if (not answer) or (a != answer[-1]):
            answer.append(a)
    return answer