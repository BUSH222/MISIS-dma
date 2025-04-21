import heapq


# n1
# TEST - ford_bellman_tests.zip

def ford_bellman(n, m, start, end, edges):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return -1

    if dist[end] == float('inf'):
        return -1

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return dist[end], path


# n, m, start, end = map(int, input().split())
# edges = []

# for _ in range(m):
#     u, v, w = map(int, input().split())
#     edges.append((u, v, w))

# result = ford_bellman(n, m, start, end, edges)

# if result == -1:
#     print(-1)
# elif result[0] == -1:  # idk why i need this but without this it doesnt work
#     print(-1)
# else:
#     dist, path = result
#     print(dist)
#     print(" ".join(map(str, path)))


# n2
# TEST - prim_tests.zip


def prim_mst(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * (n + 1)
    mst_edges = []
    total_weight = 0

    priority_queue = [(0, 1, -1)]

    while priority_queue:
        weight, current, parent = heapq.heappop(priority_queue)

        if visited[current]:
            continue

        visited[current] = True
        if parent != -1:
            mst_edges.append((parent, current))
            total_weight += weight

        for next_weight, neighbor in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(priority_queue, (next_weight, neighbor, current))

    if not all(visited[1:]):
        return -1

    mst_edges = [(min(u, v), max(u, v)) for u, v in mst_edges]
    mst_edges.sort()

    return total_weight, mst_edges


n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

result = prim_mst(n, m, edges)

if result == -1:
    print(-1)
else:
    total_weight, mst_edges = result
    print(total_weight)
    if mst_edges:
        print(' '.join(f"{u} {v}" for u, v in mst_edges))
