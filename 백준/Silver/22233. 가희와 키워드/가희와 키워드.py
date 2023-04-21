import sys
input = sys.stdin.readline
n, m = map(int, input().split())
keywords = set()
for _ in range(n):
    keywords.add(input().rstrip())
for _ in range(m):
    blogs = input().rstrip().split(",")
    for blog in blogs:
        keywords.discard(blog)
    print(len(keywords))