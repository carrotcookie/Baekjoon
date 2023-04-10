import sys

def adjacent(i):
    if a[i-1] or a[i+1] or a[i-n] or a[i+n]:
        return True
    return False

n = int(input())
a = []
area = []

for i in range(n):
    a += list(map(int, input().split()))

max_height = -sys.maxsize
for i in range(n**2):
        if a[i] > max_height:
            max_height = a[i]

rain_height = 1

while rain_height < max_height:
    for i in range(n**2):
        if a[i] <= rain_height:
            a[i] = 0
        if a[i] and adjacent(i):
