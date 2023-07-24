check = list(input().rstrip())
for i in range(len(check)):
    compare = check[i:]
    if compare == list(reversed(compare)):
        print(len(check[:i]) + len(check))
        break