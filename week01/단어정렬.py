import sys

def merge_sort(a, left, right):
    
    def _merge_sort(a, left, mid, right):
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if a[i][0] < a[j][0]:
                sorted[k] = a[i]
                i += 1
            elif a[i][0] > a[j][0]:
                sorted[k] = a[j]
                j += 1
            elif a[i][0] == a[j][0] and a[i][1] < a[j][1]:
                sorted[k] = a[i]
                i += 1
            else:
                sorted[k] = a[j]
                j += 1
            k += 1
        
        if i > mid:
            for t in range(j, right + 1):
                sorted[k] = a[t]
                k += 1
        else:
            for t in range(i, mid + 1):
                sorted[k] = a[t]
                k += 1

        for t in range(left, right + 1):
            a[t] = sorted[t]
        

    if left < right:
        sorted = [0] * n
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        _merge_sort(a, left, mid, right)

a = []
n = int(input())

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    a.append((len(tmp), tmp))

merge_sort(a, 0, n - 1)

print(a[0][1])
for i in range(1, n):
    if a[i][1] == a[i - 1][1]: continue
    print(a[i][1])