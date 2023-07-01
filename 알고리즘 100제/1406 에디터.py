import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
n = int(input())

for i in range(n):
    instruction = list(input().split())

    if instruction[0] == 'L':
        if left:
            right.append(left.pop())
    elif instruction[0] == 'D':
        if right:
            left.append(right.pop())
    elif instruction[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(instruction[1])

while right:
    left.append(right.pop())

print(*left, sep = '')