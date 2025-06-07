from collections import Counter
s = Counter(str(input()).lower())
lst = []

for alp in s.keys():
    lst.append((alp, s[alp]))

lst.sort(reverse=True, key=lambda x:x[1])

if len(lst)>1 and lst[0][1] == lst[1][1]:
    print("?")
else:
    print(lst[0][0].upper())