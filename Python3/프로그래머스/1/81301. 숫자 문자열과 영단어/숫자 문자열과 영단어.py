def solution(s):    
    # 리턴값을 정수로 통일
    
    # dictionary 생성
    replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", 
                    "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    
    # 모든 'one' ~ 'zero'를 하나씩 검사해서 replace 메소드를 사용함
    for old, new in replacements.items():
        s = s.replace(old, new)
 
    return int(s)