import sys

def recur(count, sum, add, sub, mul, div):
    global maximum
    global minimum

    if count == n:
        maximum = max(sum, maximum)
        minimum = min(sum, minimum)
        return

    if add:
        recur(count + 1, sum + a[count], add - 1, sub, mul, div)
    if sub:
        recur(count + 1, sum - a[count], add, sub - 1, mul, div)
    if mul:
        recur(count + 1, sum * a[count], add, sub, mul - 1, div)
    if div:
        recur(count + 1, int(sum / a[count]), add, sub, mul, div - 1)
        

n = int(input())
a = [int(x) for x in input().split()]
add, sub, mul, div = map(int, input().split())
maximum = -sys.maxsize
minimum = sys.maxsize

recur(1, a[0], add, sub, mul, div)
print(maximum, minimum, sep='\n')