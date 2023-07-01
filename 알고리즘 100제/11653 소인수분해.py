import sys
input = sys.stdin.readline

n = int(input())

i = 2
while n != 1:
    if n % i:
        i += 1
        continue

    print(i)
    n //= i
    i = 2