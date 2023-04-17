import sys

a = []

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
                print(a.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(a))
        elif command == 'empty':
            if len(a):
                print(0)
            else:
                print(1)
        elif command == 'top':
            if len(a):
                print(a[-1])
            else:
                print(-1)