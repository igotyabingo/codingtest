# 시간 포맷의 비교 - 초 단위로 통일한다. 

def solution(video_len, pos, op_start, op_end, commands):
    # 기본값 파싱
    a, b = [int(i) for i in video_len.split(':')]
    video_len = a*60 + b
    a, b = [int(i) for i in pos.split(':')]
    pos = a*60 + b
    a, b = [int(i) for i in op_start.split(':')]
    op_start = a*60 + b
    a, b = [int(i) for i in op_end.split(':')]
    op_end = a*60 + b
    
    # 초기값이 오프닝 내부인지 확인
    pos = inOpening(op_start, op_end, pos)
    for cmd in commands:
        if cmd == "prev":
            pos -= 10
            if(pos < 0):
                pos = 0
        elif cmd == "next":
            pos += 10
            if(pos > video_len):
                pos = video_len
        # 매번 오프닝 내부인지 확인해야 한다.
        pos = inOpening(op_start, op_end, pos)
    
    # 시간 포맷으로 리턴한다.
    nowm, nows = pos//60, pos%60
    if nowm < 10 and nows < 10:
        return f'0{nowm}:0{nows}'
    elif nows < 10:
        return f'{nowm}:0{nows}'
    elif nowm < 10:
        return f'0{nowm}:{nows}'
    else:
        return f'{nowm}:{nows}'
            
def inOpening(op_start, op_end, now):
    if(op_start <= now and now <= op_end):
        now = op_end
    return now
    
    