from bisect import bisect_left

def solution(info, query):
    db = dict()
    answer = []

    for language in ["cpp", "java", "python"]:
        for group in ["backend", "frontend"]:
            for experience in ["junior", "senior"]:
                for food in ["chicken", "pizza"]:
                    key = ' '.join([language, group, experience, food])
                    db[key] = []
    
    for i in info:
        data = i.split(" ")
        db[' '.join(data[:-1])].append(int(data[-1]))
    
    for key in db:
        db[key].sort()

    for q in query:
        keys = []
        data = q.split(" ")

        if data[0] == "-":
            keys.append("cpp ")
            keys.append("java ")
            keys.append("python ")
        else:
            keys.append(data[0]+ " ")

        if data[2] == "-":
            tmp = []
            for i, k in enumerate(keys):
                keys[i] = k + "backend "
                tmp.append(k + "frontend ")
            keys += tmp
        else:
            for i, k in enumerate(keys):
                keys[i] = k + data[2] + " "

        if data[4] == "-":
            tmp = []
            for i, k in enumerate(keys):
                keys[i] = k + "junior "
                tmp.append(k + "senior ")
            keys += tmp
        else:
            for i, k in enumerate(keys):
                keys[i] = k + data[4] + " "
        
        if data[6] == "-":
            tmp = []
            for i, k in enumerate(keys):
                keys[i] = k + "pizza"
                tmp.append(k + "chicken")
            keys += tmp
        else:
            for i, k in enumerate(keys):
                keys[i] = k + data[6]
        
        count = 0
        for key in keys: 
            idx = bisect_left(db[key], int(data[7]))
            count += len(db[key]) - idx
        
        answer.append(count)
            
    return answer