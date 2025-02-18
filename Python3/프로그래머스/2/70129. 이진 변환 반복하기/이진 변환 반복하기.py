def solution(s):
    # 이진 변환의 횟수 a
    a = 0
    # 변환 과정에서 제거한 모든 0의 개수 b
    b = 0
    # s가 1이 될때까지 이진변환 과정을 반복한다.
    while(s != '1'):
        a += 1
        c = s.count('1')    # c를 이진법으로 표현해 s값을 업데이트하면 된다.
        b += len(s)-c
        s = convert(c)

    return [a, b]

def convert(c): # 10진법의 '정수'를 2진법의 '문자열'로 변환하는 함수 작성
    ans = ''
    a = c
    while(a != 1):
        a, b = a//2, a%2
        ans += str(b)
    ans += '1'
    return ans[::-1]


# 파이썬 내장함수 bin(): 10진수 int를 2진수 문자열 '0b{2진수}'로 변환해 출력한다. bin(c)[2:]를 파싱하면 되는 것이다.
