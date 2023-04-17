import sys

# 1.
# stack = []

# for _ in range(int(input())):
#     n = int(sys.stdin.readline())

#     if not n:
#         stack.pop()
#         continue

#     stack.append(n)

# print(sum(stack))

#########################################################################

# 2.
stack = []
sum = 0

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    if not n:
        sum -= stack.pop()[0]
        continue
    
    sum += n
    stack.append((n, sum))

print(sum)