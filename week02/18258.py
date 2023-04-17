# import sys

# a = []

# for _ in range(int(input())):
#     tmp = sys.stdin.readline().split()
#     n = len(tmp)

#     if n == 2:
#         num = int(tmp[1])
#         a.append(num)
#     else:
#         command = tmp[0]

#         if command == 'pop':
#             if len(a):
#                 print(a[0])
#                 del a[0]
#             else:
#                 print(-1)
#         elif command == 'size':
#             print(len(a))
#         elif command == 'empty':
#             if len(a):
#                 print(0)
#             else:
#                 print(1)
#         elif command == 'front':
#             if len(a):
#                 print(a[0])
#             else:
#                 print(-1)
#         elif command == 'back':
#             if len(a):
#                 print(a[-1])
#             else:
#                 print(-1)

##############################################################################################################

from collections import deque
import sys

a = deque()

for _ in range(int(input())):
    tmp = sys.stdin.readline().split()
    n = len(tmp)

    if n == 2:
        num = int(tmp[1])
        a.append(num)
    else:
        command = tmp[0]

        if command == 'pop':
            if len(a):
                print(a.popleft())
            else:
                print(-1)
        elif command == 'size':
            print(len(a))
        elif command == 'empty':
            if len(a):
                print(0)
            else:
                print(1)
        elif command == 'front':
            if len(a):
                print(a[0])
            else:
                print(-1)
        elif command == 'back':
            if len(a):
                print(a[-1])
            else:
                print(-1)