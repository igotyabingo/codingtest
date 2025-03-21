def solution(s):
    min_len = len(s)
    
    for l in range(1, len(s)//2 + 1):
        result = ''
        tmp = 0
        prev = ''
        for i in range(0, len(s), l):
            if s[i:i+l] == prev:
                tmp += 1
            else:
                if tmp > 1:
                    result += f'{tmp}{prev}'
                else:
                    result += prev
                tmp = 1
                prev = s[i:i+l]

        if tmp > 1:
            result += f'{tmp}{prev}'
        else:
            result += s[i:]
        min_len = min(min_len, len(result))

    return min_len 