import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    x, y = heapq.heappop(cards), heapq.heappop(cards)
    new_number = x + y
    heapq.heappush(cards, new_number)
    heapq.heappush(cards, new_number)

print(sum(cards))