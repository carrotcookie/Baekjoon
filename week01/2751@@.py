# import sys

# def quick_sort(a, left, right):
#     pl = left
#     pr = right
#     x = a[(left + right) // 2]

#     while pl <= pr:
#         while a[pl] < x: pl += 1
#         while a[pr] > x: pr -= 1

#         if pl <= pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl += 1
#             pr -= 1

#     if left < pr: quick_sort(a, left, pr)
#     if pl < right: quick_sort(a, pl, right)

# a = []
# N = int(sys.stdin.readline().rstrip())
# for _ in range(N):
#     a.append(sys.stdin.readline().rstrip())
# quick_sort(a, 0, len(a)-1)
# for i in a:
#     print(i)

import sys

a = []
n = int(input())

for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

for num in a:
    print(num)