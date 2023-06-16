from collections import defaultdict
def solution(numbers, hand):
    answer = ''
    keyPad = defaultdict(list)
    keyPad[1], keyPad[2], keyPad[3] = [0, 0], [0, 1], [0, 2]
    keyPad[4], keyPad[5], keyPad[6] = [1, 0], [1, 1], [1, 2]
    keyPad[7], keyPad[8], keyPad[9] = [2, 0], [2, 1], [2, 2]
    keyPad[0] = [3, 1]
    left , right = [3, 0], [3, 2]
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = keyPad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right = keyPad[number]
        else:
            calcLeft = abs(left[0] - keyPad[number][0]) + abs(left[1] - keyPad[number][1])
            calcRight = abs(right[0] - keyPad[number][0]) + abs(right[1] - keyPad[number][1])
            if calcLeft > calcRight :
                answer += 'R'
                right = keyPad[number]
            elif calcLeft < calcRight:
                answer += 'L'
                left = keyPad[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = keyPad[number]
                else:
                    answer += 'L'
                    left = keyPad[number]
    return answer