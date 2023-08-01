n, k = map(int, input().split())
lst = list(map(int, input().split()))
start = 0
end = k
num = sum(lst[start: end])
answer = num
for i in range(1, n-k+1):
    num = num - lst[start] + lst[end]
    start += 1
    end += 1
    answer = max(answer, num)
print(answer)