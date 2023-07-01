# 재귀
# 3중 for문
# combination

# 1. 재귀
# import sys
# input = sys.stdin.readline

# def recur(idx, count):
#     global answer

#     if count == 3:
#         if sum(selection) <= m:
#             answer = max(answer, sum(selection))
#             return

#     for j in range(idx + 1, len(card_lst)):
#         selection.append(card_lst[j])
#         recur(j, count + 1)
#         selection.pop()

# n, m = map(int, input().split())
# card_lst = sorted(list(map(int, input().split())))
# selection = []
# answer = 0

# for i in range(len(card_lst) - 2):
#     selection.append(card_lst[i])
#     recur(i, 1)
#     selection.pop()

# print(answer)

###########################################################################################################################

# 2. combinations
import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
card_lst = list(map(int, input().split()))
nC3 = itertools.combinations(card_lst, 3)
answer = 0

for case in nC3:
    if sum(case) <= m:
        answer = max(answer, sum(case))

print(answer)