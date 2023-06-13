import sys
import heapq
input = sys.stdin.readline

n = int(input())
score = 0
assignments = []

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    
    if info[0] == 0:
        if assignments:
            assignment = heapq.heappop(assignments)
            assignment[3] -= 1
            if assignment[3] > 0:
                heapq.heappush(assignments, assignment)
            else:
                 score += assignment[2]
    
    else:
        assignment = [-i] + info
        assignment[3] -= 1
        if assignment[3] > 0:
            heapq.heappush(assignments, assignment)
        else:
            score += assignment[2]

print(score)