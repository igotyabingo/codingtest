import re
def solution(new_id):
    # 각 단계별로 차례로 처리하면 된다. 문자열 관련 함수
    
    new_id = new_id.lower() # 1단계
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)    # 2단계
    new_id = re.sub(r"\.+", ".", new_id)    # 3단계
    if new_id and new_id[0] == '.':    # 4단계
        if len(new_id) >= 2:
            new_id = new_id[1:]
        else:
            new_id = ''
    if new_id and new_id[-1] == '.':
        if len(new_id) >= 2:
            new_id = new_id[:-1]
        else:
            new_id = ''
    if not new_id:  # 5단계
        new_id = 'a'
    if len(new_id) >=16:    # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2: #7단계
        l = new_id[-1]
        for _ in range(3-len(new_id)):
            new_id+=l
            
    return new_id