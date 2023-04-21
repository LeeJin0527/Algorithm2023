n = int(input())
budgetList = list(map(int, input().split()))
total = int(input())
start, end = 0, max(budgetList)
answer = 0
if sum(budgetList) <= total:
    print(max(budgetList))
else:
    while start <= end:
        mid = (start + end) // 2
        checkCurrentBudget = 0
        for budget in budgetList:
            if budget < mid:
                checkCurrentBudget += budget
            else:
                checkCurrentBudget += mid
        if checkCurrentBudget > total:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    print(answer)