str = input()
answer = ''
for value in list(str):
    if value.isupper():
        answer += value.lower()
    else:
        answer += value.upper()
print(answer)        
