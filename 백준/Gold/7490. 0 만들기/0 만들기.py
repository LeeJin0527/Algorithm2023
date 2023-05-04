import sys
from itertools import product
import copy
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    lst = [str(index) for index in range(1, n+1)]
    sign = ['+', '-', '']
    result = []
    for si in list(product(sign, repeat = n-1)):
        answer = 0
        check = copy.deepcopy(lst)
        for index, each in enumerate(si):
            if each == '+':
                check.insert(2*index-1, '+')
            elif each == '-':
                check.insert(2*index-1, '-')
            else:
                check.insert(2*index-1, ' ')
        origin = ''.join(check)
        check = ''.join(check)
        dividedByPlus = list(check.split('+'))
        for divided in dividedByPlus:
            divided = divided.replace(" ", "")
            if '-' in divided:
                temp = divided.split('-')
                number = int(temp[0])
                for index in range(1, len(temp)):
                    number -= int(temp[index])
                answer += number
            else:
                answer += int(divided)
        if answer == 0:
            result.append(origin)
    result.sort()
    for res in result:
        print(res)
    print()