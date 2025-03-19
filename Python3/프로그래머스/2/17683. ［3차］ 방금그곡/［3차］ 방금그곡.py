dic = {'A#': 'a', 'B#': 'b', 'C#': 'c', 'D#': 'd', 'E#': 'e', 'F#': 'f', 'G#': 'g'}

def translate(string):
    for alp in dic:
        string = string.replace(alp, dic[alp])
    
    return string

def calculate(time):
    hh, mm = time.split(':')

    return int(hh)*60 + int(mm)

def solution(m, musicinfos):
    answer = []
    m = translate(m)

    for music in musicinfos:
        start, end, name, info = music.split(',')
        info, start, end = translate(info), calculate(start), calculate(end)
        target = ''

        if len(info) >= end-start:
            target = info[:(end-start)]
        else:
            target = info*((end-start)//len(info)) + info[:(end-start)%len(info)]
        if m in target:
            answer.append((name, end-start))
    
    if not answer: return '(None)'
    if len(answer) > 1: answer.sort(key = lambda x:x[1], reverse=True)
    
    return answer[0][0]