def solution(skill, skill_trees):
    answer = 0
    
    # 순서가 정해진 알파벳과 그렇지 않은 알파벳을 빨리 구분하자
    isChecked = dict()
    for i in range(26):
        isChecked[chr(ord('A')+i)] = False
    for i in skill:
        isChecked[i] = True
        
    for i in skill_trees:
        answer += 1
        j = 0
        for s in i:
            if isChecked[s]:
                if skill[j] == s:
                    j += 1
                else:
                    answer -= 1
                    break
                    
    return answer