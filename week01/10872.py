# 1. while문 이용
# n = int(input())
# result = 1

# if (n==0) or (n==1):
#     print(1)
# else:
#     while n:
#         result *= n
#         n -= 1
#     print(result)

# 2. 재귀함수 이용
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input())

if n == 0:
    print(1)
else:
    print(factorial(n))