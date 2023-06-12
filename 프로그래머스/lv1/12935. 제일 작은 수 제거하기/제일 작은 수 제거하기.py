def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    check = min(arr)
    idx = arr.index(check)
    answer = arr[:idx] + arr[idx+1:]
    return answer