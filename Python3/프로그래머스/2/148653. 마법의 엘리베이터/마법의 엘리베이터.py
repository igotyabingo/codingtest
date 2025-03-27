def solution(storey):
    count = 0 

    while True:
        s = str(storey)
        if storey / 10**(len(s)-1) >= 5.5: # 자릿수 +1 
            storey = 10**len(s) - storey
            count += 1
        else: # 자릿수 유지
            if len(s) == 1: # 한자리 수일 경우
                count += storey
                break
            else:
                k = int(s[1:])
                if k / 10**(len(s)-2) >= 5.5: # 올림
                    tmp = int(s[0])+1
                    count += tmp
                    storey = tmp*10**(len(s)-1) - storey
                else:
                    tmp = int(s[0])
                    count += tmp
                    storey = storey - tmp*10**(len(s)-1)

    return count