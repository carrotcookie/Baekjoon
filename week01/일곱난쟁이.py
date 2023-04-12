a = []
b = []
for _ in range(9):
    a.append(int(input()))

def recursive(start, cnt):
    if cnt == 7:
        if sum(b) == 100:
            for i in b:
                print(i)
            exit()
        return
    
    for i in range(start, 9):
        b.append(a[i])
        recursive(i+1, cnt + 1)
        b.pop()

a.sort()
recursive(0, 0)