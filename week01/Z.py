def z_curve():
    global i
    global j
    global count

    size = 2**(n-1)

    while size > 1:
        if i < size and j < size:
            count += 0
        elif i < size and j >= size:
            count += size**2
            j -= size
        elif i >= size and j < size:
            count += size**2 * 2 
            i -= size
        else:
            count += size**2 * 3
            i -= size
            j -= size
        size //= 2

    if i == 0 and j == 0:
        print((count))
    elif i == 0 and j == 1:
        print((count + 1))
    elif i == 1 and j == 0:
        print((count + 2))
    else:
        print((count + 3))

n, i, j = map(int, input().split())
count = 0
z_curve()