import sys

# 1.
# for _ in range(int(input())):
#     a = sys.stdin.readline().rstrip()
#     stack = []

#     stack.append(a[0])
#     for ch in a[1:]:
#         if stack and stack[-1] == '(' and ch == ')':
#             stack.pop()
#             continue
#         stack.append(ch)
        
#     print('NO' if stack else 'YES')

###########################################################################

# 2.
for _ in range(int(input())):
    a = sys.stdin.readline().rstrip()
    
    while '()' in a:
        a = a.replace('()', '')
    
    print('NO' if a else 'YES')