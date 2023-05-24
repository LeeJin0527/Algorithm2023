def solution(array):

    array = list(array)
    index = 0
    for idx, value in enumerate(array):
        if value == ' ':
            index = 0
        elif index % 2 == 0:
            array[idx] = value.upper()
            index += 1
        elif index % 2 == 1:
            array[idx] = value.lower()
            index += 1
    
    return ''.join(array)