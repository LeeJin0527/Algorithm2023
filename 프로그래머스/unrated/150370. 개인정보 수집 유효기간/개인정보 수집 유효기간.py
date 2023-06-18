from collections import defaultdict
def solution(today, terms, privacies):
    tYear, tMonth, tDay = today.split(".")
    answer = []
    check = defaultdict(int)
    for term in terms:
        x, y = term.split(" ")
        check[x] = int(y)
    for index, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        year, month, day = date.split(".")
        year, month, day = int(year), int(month), int(day)
        temp = int(month) + int(check[term])

        if temp > 12:
            month = temp % 12
            if month == 0:
                month = 12
                year -= 1
            year += temp // 12
        else:
            month = temp
            
        day -= 1
        if day == 0:
            month -= 1
            day = 28
        print(year, month, day)

        if year < int(tYear):
            answer.append(index+1)
            continue
        if year <= int(tYear) and month < int(tMonth):
            answer.append(index+1)
            continue
        if year <= int(tYear) and month <= int(tMonth) and day < int(tDay):
            answer.append(index+1)
            continue

    return answer