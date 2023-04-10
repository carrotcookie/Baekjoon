# 1.
# import sys

# height_lst = [int(input()) for _ in range(9)]
# height_lst.sort()
# sum = sum(height_lst)

# for i in range(0, 9):
#     for j in range(i+1, 9):
#         if height_lst[i] + height_lst[j] == sum - 100:
#             for k in range(9):
#                 if k == i or k == j: continue
#                 print(height_lst[k])
#             sys.exit()

# 2.
# 7개 짜리 리스트를 만든다
# 원본 리스트의 0번 인덱스부터 7개짜리에 넣어간다
# 총 7번을 넣었을 때 sum = 100 이면 출력하고 스탑
# import sys

# org_lst = [int(input()) for _ in range(9)]
# org_lst.sort()
# post_lst = []

# def recursive(count, start):
#     if count > 6:
#         if sum(post_lst) == 100:
#             for h in post_lst:
#                 print(h)
#             sys.exit()
#         else:
#             return
    
#     for i in range(start, 9):
#         post_lst.append(org_lst[i])
#         recursive(count+1, i+1)
#         post_lst.pop()

# recursive(0, 0)