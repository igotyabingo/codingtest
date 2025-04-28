def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)

    for i in range(len(A)):
        if B[0] > A[i]:
            answer += 1
            B.pop(0)
        else:
            B.pop(-1)
    
    return answer