# 1. 시간초과
# import sys
# input = sys.stdin.readline

# input_str = input().rstrip()
# explosion_str = input().rstrip()

# while explosion_str in input_str:
#     tmp = input_str.split(explosion_str)
#     input_str = ''.join(st for st in tmp)

# print(input_str if input_str else 'FRULA')

################################################################################################################

# 2. 시간초과
# import sys
# input = sys.stdin.readline

# input_str = input().rstrip()
# explosion_str = input().rstrip()
# stack = ''

# for ch in input_str:
#     stack += ch

#     if explosion_str in stack:
#         stack = stack.replace(explosion_str, '')

# print(stack if stack else 'FRULA')

################################################################################################################

# 3.
import sys
input = sys.stdin.readline

input_str = input().rstrip()
explosion_str = list(input().rstrip())
explosion_len = len(explosion_str)
stack = []
count = 0

for ch in input_str:
    stack.append(ch)

    if len(stack) >= explosion_len:
        if stack[len(stack)-explosion_len:] == explosion_str:
            for _ in range(explosion_len):
                stack.pop()

print(*stack if stack else 'FRULA', sep = '')