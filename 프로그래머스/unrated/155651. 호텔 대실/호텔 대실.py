from collections import defaultdict
def solution(book_time):
    book_time.sort()
    answer = 0
    check = defaultdict(int)
    for start, end in book_time:

        start_hour, start_minute = start.split(":")
        end_hour, end_minute = end.split(":")
        for x in range(int(start_hour), int(end_hour)+1):
            if x == int(start_hour) and x == int(end_hour):
                for y in range(int(start_minute), int(end_minute) + 10):
                    if y >= 60:
                        x = int(end_hour) + 1
                        y -= 60
                    x = str(x).zfill(2)
                    y = str(y).zfill(2)
                    check[x+y] += 1
            elif x == int(start_hour):
                for y in range(int(start_minute), 60):
                    x = str(x).zfill(2)
                    y = str(y).zfill(2)
                    check[x+y] += 1
            elif x == int(end_hour):
                for y in range(0, int(end_minute)+10):
                    if y >= 60:
                        x = int(end_hour) + 1
                        y -= 60
                    x = str(x).zfill(2)
                    y = str(y).zfill(2)
                    check[x+y] += 1
            else:
                for y in range(0, 60):
                    x = str(x).zfill(2)
                    y = str(y).zfill(2)
                    check[x+y] += 1

    for che in check:
        if check[che] > answer:
            answer = check[che]
    return answer