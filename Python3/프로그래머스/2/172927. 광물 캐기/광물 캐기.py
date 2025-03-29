def solution(picks, minerals):
    dia, iron, stone = picks
    round = (dia+iron+stone)
    queue = [[dia, iron, stone, 0]]
    k = 0
    
    for _ in range(round):
        l = len(queue)
        for _ in range(l):
            dia, iron, stone, count = queue.pop(0)
            d, i, s = 0, 0, 0
            
            if dia > 0: d += len(minerals[k:k+5])
            bool_i, bool_s = iron > 0, stone > 0
            
            for m in minerals[k:k+5]:
                if m == "diamond":
                    i += 5*(bool_i)
                    s += 25*(bool_s)
                elif m == "iron":
                    i += 1*(bool_i)
                    s += 5*(bool_s)
                else:
                    i += 1*(bool_i)
                    s += 1*(bool_s)
            
            if d != 0: 
                queue.append([dia-1, iron, stone, count+d])
            if i != 0: 
                queue.append([dia, iron-1, stone, count+i])
            if s != 0:
                queue.append([dia, iron, stone-1, count+s])
            
        k += 5
        if k >= len(minerals): break
    
    queue.sort(key = lambda x: x[3])
    return queue[0][3]