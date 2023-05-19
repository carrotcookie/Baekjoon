import sys
input = sys.stdin.readline

def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        total = 0

        for budget in budgets:
            if budget < mid:
                total += budget
            else:
                total += mid
        
        if total <= limit:
            left = mid + 1
        else:
            right = mid - 1

    print(right)


n = int(input())
budgets = list(map(int, input().split()))
limit = int(input())

max_budget = max(budgets)

if sum(budgets) <= limit:
    print(max_budget)
else:
    binary_search(0, max_budget)