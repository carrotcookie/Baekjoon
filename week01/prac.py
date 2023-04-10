# 버블정렬
def bubble_sort(a):
    n = len(a)

    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]

# 선택정렬
def selection_sort(a):
    # 가장 작은걸 맨 앞으로
    n = len(a)

    for i in range(n):
        min = 10000
        index = 0
        for j in range(i, n):
            if min > a[j]:
                min = a[j]
                index = j
        a[i], a[index] = a[index], a[i]


a = [5, 3, 8, 1, 10, 2, 4, 7, 6, 9]

print(f'변경 전: {a}')

# bubble_sort(a)
selection_sort(a)

print(f'변경 후: {a}')