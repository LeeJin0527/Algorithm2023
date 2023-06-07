n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])
map = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    # 이동할게요
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + dx[cd] * cs) % n
        nc = (cc + dy[cd] * cs) % n
        map[nr][nc].append([cm, cs, cd])
    for i in range(n):
        for j in range(n):
            # 2개 이상
            if len(map[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(map[i][j])
                while map[i][j]:
                    _m, _s, _d = map[i][j].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:  # 질량 0이면 소멸
                    for d in nd:
                        fireballs.append([i, j, sum_m // 5, sum_s // cnt, d])
            # 한개
            elif len(map[i][j]) == 1:
                fireballs.append([i, j] + map[i][j].pop())

print(sum([f[2] for f in fireballs]))
