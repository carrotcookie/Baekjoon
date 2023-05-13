import sys
input = sys.stdin.readline

def recur(len, start, end):
    if len == 1:
        return
    
    unit = len // 3
    
    recur(len // 3, start, start + unit - 1)
    for i in range(start + unit, start + 2 * unit):
        a[i] = ' '
    recur(len // 3, end - unit + 1, end)

while True:
    try:
        n = int(input())
        a = ['-'] * (3 ** n)
        recur(3 ** n, 0, 3 ** n - 1)
        print(*a, sep = '')
    except:
        break