import sys
input = sys.stdin.readline

formula = input().rstrip().split('-')
nums = []
ans = 0

for val in formula:
    sum = 0
    two_nums = val.split('+')

    for num in two_nums:
        sum += int(num)
    
    nums.append(sum)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]
print(ans)