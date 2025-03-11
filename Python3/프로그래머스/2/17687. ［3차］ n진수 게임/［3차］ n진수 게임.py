def solution(n, t, m, p):
    record, i, answer = '', -1, ''
    
    # 튜브가 말해야 할 숫자"만" 계산해내는 것은 불가능하다.
    while(len(record)<p+(t-1)*m):
        i += 1
        record += convert(n, i)
    
    for i in range(p-1, p+(t-1)*m, m):
        answer += record[i]
    
    return answer

# 진법 변환하는 함수
def convert(n, i):
    if i == 0: return '0'
    answer = ''
    digit = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while(i > 0):
        i, k = i // n, i % n
        answer += digit[k]
        
    return answer[::-1]