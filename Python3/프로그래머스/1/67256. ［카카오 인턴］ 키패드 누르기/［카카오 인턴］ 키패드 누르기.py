def solution(numbers, hand):
    answer = ''
    # 위치를 어떻게 숫자화해서 거리 계산할 것인지 생각: '행'과 '열' 차이의 절댓값
    dic = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    
    # 왼쪽 손가락과 오른쪽 손가락의 '현재' 위치를 저장하고 계속 업데이트해야 한다.
    l, r = (3, 0), (3, 2)
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l = dic[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            r = dic[i]
        else:
            left = calculate(l, dic[i])
            right = calculate(r, dic[i])
            if(left<right):
                answer += 'L'
                l = dic[i]
            elif(left>right):
                answer += 'R'
                r = dic[i]
            else:
                # hand는 거리가 같을때만 판단기준으로 사용한다.
                if hand == "right":
                    answer += 'R'
                    r = dic[i]
                else:
                    answer += 'L'
                    l = dic[i]
    return answer

def calculate(a, b):    
    # 좌표간의 거리계산하는 함수
    x1, y1 = a
    x2, y2 = b
    
    return abs(x1-x2) + abs(y1-y2)