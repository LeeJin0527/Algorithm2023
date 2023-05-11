def solution(number, k):
    stack = []
    for num in number:
        if stack and stack[-1] < num:
            while stack and k > 0 and stack[-1] < num:
                k -= 1
                stack.pop()
        stack.append(num)

    return ''.join(stack)[:len(number)-k]