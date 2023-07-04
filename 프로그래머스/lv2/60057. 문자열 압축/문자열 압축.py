def solution(s):
    if len(s) == 1:
        return 1
    answer = int(1e9)
    for index in range(1, len(s) // 2 + 1):
        cnt = 1
        compress = ''
        prev = s[0 : index]

        for j in range(index, len(s), index):
            if prev == s[j : index + j]:
                cnt += 1
            else:
                if cnt >= 2:
                    compress += str(cnt) + prev
                else:
                    compress += prev
                prev = s[j : index + j]
                cnt = 1
        if cnt >= 2:
            compress += str(cnt) + prev
        else:
            compress += prev
        answer = min(answer, len(compress))
                
    return answer