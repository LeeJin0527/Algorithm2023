import copy
n = int(input())
words = []
for _ in range(n):
    words.append(list(input().rstrip()))
origin = words[0]
words = words[1:]
answer = 0
for index in range(len(words)):
    compare = words[index]
    if len(compare) >= len(origin):
        for each in origin:
            if each in compare:
                compare.remove(each)
        if len(compare) == 1 or len(compare) == 0:
            answer += 1
    else:
        temp = copy.deepcopy(origin)
        for comp in compare:
            if comp in temp:
                temp.remove(comp)
        if len(temp) == 1:
            answer += 1
print(answer)