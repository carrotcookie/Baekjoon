import sys

# 1. 스택
# a = []
# stack = []

# for _ in range(int(input())):
#     h = int(sys.stdin.readline())
#     a.append(h)

#     while stack and stack[-1] <= h:
#         stack.pop()
    
#     stack.append(h)

# print(len(stack))

#########################################################################

# 2.
n = int(input())
a = [int(sys.stdin.readline()) for _ in range(n)]

# 보는 방향에서부터 진행하면서 큰게 나올때마다 카운팅
before = 0
count = 0
for h in a[::-1]:
    if h > before:
        count += 1
        before = h

print(count)