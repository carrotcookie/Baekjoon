def hanoi(n, start, end, via):
    if n==0:
        return
    hanoi(n-1, start, via, end)
    print(start, end)
    hanoi(n-1, via, end, start)

n = int(input())
count = 2**n - 1

if n > 20:
    print(count)
else:
    print(count)
    hanoi(n, 1, 3, 2)