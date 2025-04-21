# n1
# TEST - kan_tests.zip

from collections import deque
import heapq  # I did heaps manually in 3-dfs-bfs.py


def kahn_topological_sort(n, adjacency_list):
    in_degree = [0] * (n + 1)
    for neighbors in adjacency_list:
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    zero_in_degree = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

    topological_order = []
    visited_count = 0

    while zero_in_degree:
        current = zero_in_degree.popleft()
        topological_order.append(current)
        visited_count += 1
        for neighbor in adjacency_list[current - 1]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)
    if visited_count != n:
        return -1

    return topological_order


# n = int(input())
# adjacency_list = []

# for i in range(1, n + 1):
#     line = list(map(int, input().split()))
#     adjacency_list.append(line[1:])
# result = kahn_topological_sort(n, adjacency_list)

# if result == -1:
#     print(-1)
# else:
#     print(" ".join(map(str, result)))


# n2
# TEST - bfs_path_tests.zip


def bfs_shortest_path(n, start, end, adjacency_list):

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    dist = [-1] * (n + 1)

    queue = deque([start])
    visited[start] = True
    dist[start] = 0

    while queue:
        current = queue.popleft()

        for neighbor in adjacency_list[current - 1]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)
                if neighbor == end:
                    break

    if not visited[end]:
        return -1

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return dist[end], path


# n, start, end = map(int, input().split())
# adjacency_list = []

# for i in range(1, n + 1):
#     line = list(map(int, input().split()))
#     adjacency_list.append(line[1:])

# result = bfs_shortest_path(n, start, end, adjacency_list)

# if result == -1:
#     print(-1)
# else:
#     dist, path = result
#     print(dist)
#     print(" ".join(map(str, path)))

# n3
# TEST - dijkstra_tests.zip


def dijkstra_shortest_path(n, start, end, adjacency_list):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > dist[current_vertex]:
            continue

        for i in range(0, len(adjacency_list[current_vertex - 1]), 2):
            neighbor = adjacency_list[current_vertex - 1][i]
            weight = adjacency_list[current_vertex - 1][i + 1]
            new_dist = dist[current_vertex] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_dist, neighbor))

    if dist[end] == float('inf'):
        return -1

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return dist[end], path


n, start, end = map(int, input().split())
adjacency_list = []

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    adjacency_list.append(line[1:])

result = dijkstra_shortest_path(n, start, end, adjacency_list)

if result == -1:
    print(-1)
else:
    dist, path = result
    print(dist)
    print(" ".join(map(str, path)))