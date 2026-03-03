def solution(arr):
    stack = [arr[0]]
    # use stack: 매 입력마다 top 원소와의 비교
    
    for element in arr[1:]:
        if stack[-1] != element:
            stack.append(element)
    return stack