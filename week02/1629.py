# while True:
#     a, b, c = map(int, input().split())
#     print(a ** b % c)
#     print()


# while True:
#     a, b, c = map(int, input().split())
#     a_square = a
#     arr = []
#     did_find = False
#     is_special = False

#     while not did_find:
#         value = a_square % c

#         if arr.count(value):
#             did_find = True
#             if arr[-1] == value:
#                 is_special = True
#         else:
#             arr.append(value)
#             a_square *= a

#     if is_special:
#         print(arr[-1])
#     else: 
#         print(arr[b % len(arr) - 1])
#     print(arr)


# def func(b, c):

#     if b == 1:
#         return a % c

#     left = b // 2
#     right = b - b // 2 

#     return func(left, c) * func(right, c) % c

# a, b, c = map(int, input().split())
# print(func(b, c))

import sys

def func(b):
  if b == 1:
      return a % c
  else:
      tmp = func(b//2)

      if b % 2 == 0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp * a) % c

a, b, c = map(int,sys.stdin.readline().split())

print(func(b))