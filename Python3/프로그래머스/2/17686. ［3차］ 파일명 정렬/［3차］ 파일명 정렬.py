import re

def solution(files):
    files = [splitt(file) for file in files]
    # 파일명을 각각 splitt 함수를 적용하여 (전체파일명, HEAD, NUMBER)로 다시 저장한다.
    
    # HEAD 기준 비교 -> NUMBER 기준 비교
    files.sort(key = lambda x:(x[1], x[2]))
    return [file[0] for file in files]

def splitt(file):   # 파일명을 HEAD와 NUMBER로 분리한다.
    # 정규표현식 
    match = re.match(r"(\D*)(\d+)(\D*)", file)
    head = match.group(1).lower()
    return (file, head, int(match.group(2)))