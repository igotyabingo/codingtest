def solution(number, k):

    # 앞에서 한자리씩 차근차근 ("뒤에 충분한 개수(l개)의 수가 남아있다"를 보장하는 숫자를 찾아야 한다.)
    l = len(number)-k-1
    target = len(number)-k
    answer = ""

    while(len(answer) < target): # while문 반복 한번 = 한 자리 정함
        for i in range(9, -1, -1):
            try:
                idx = number.index(str(i))
                if len(number)-idx > l:
                    number = number[idx+1:]
                    l -= 1
                    answer += str(i)
                    break
            except:
                pass

    return answer