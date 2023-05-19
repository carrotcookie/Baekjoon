import sys
input = sys.stdin.readline

room = input().rstrip()
num_arr = [0] * 10

for ch in room:
    num = int(ch)
    
    if num == 6 or num == 9:
        if num_arr[6] > num_arr[9]:
            num_arr[9] += 1
        else:
            num_arr[6] += 1
    
    else:
        num_arr[num] += 1

print(max(num_arr))