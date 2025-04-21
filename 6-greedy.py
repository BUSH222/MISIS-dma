# 1 - Покупка предметов

def max_items_can_buy(k, prices):
    count = 0
    for price in prices:
        if k >= price:
            k -= price
            count += 1
        else:
            break
    return count


# _, k = map(int, input().split())
# prices = list(map(int, input().split()))

# print(max_items_can_buy(k, prices))


# 2 - Расписание задач

import heapq

def max_total_reward(tasks):
    min_heap = []

    for d, w in tasks:
        if len(min_heap) < d:
            heapq.heappush(min_heap, w)
        elif min_heap and min_heap[0] < w:
            heapq.heappushpop(min_heap, w)
    
    return sum(min_heap)


# n = int(input())
# tasks = [tuple(map(int, input().split())) for _ in range(n)]
# print(max_total_reward(tasks))

# 3 - Непересекающиеся отрезки

def max_uncrossed_things(segments):
    count = 0
    last_end = -float('inf')

    for l, r in segments:
        if l >= last_end:
            count += 1
            last_end = r

    return count

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(max_uncrossed_things(segments))
