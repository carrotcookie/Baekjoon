A, B = map(str, input().split())

newA = int(A[::-1])
newB = int(B[::-1])

if newA > newB:
    print(newA)
else:
    print(newB)