from collections import deque

# n1
# TEST - bfs_tests.zip


def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


# N = int(input())
# graph = {i: [] for i in range(1, N + 1)}

# for i in range(1, N + 1):
#     line = list(map(int, input().split()))
#     graph[i] = line[1:]

# result = bfs(graph, 1)
# print(' '.join(map(str, result)))


# n2
# TEST - dfs_tests.zip


def dfs(graph, start):
    visited = [False] * (len(graph) + 1)
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return result


# N = int(input())
# graph = {i: [] for i in range(1, N + 1)}

# for i in range(1, N + 1):
#     line = list(map(int, input().split()))
#     graph[i] = line[1:]

# result = dfs(graph, 1)
# print(' '.join(map(str, result)))


# n3
# TEST - ??

def count_connected_components(graph, n):
    visited = [False] * (n + 1)
    components = 0

    def dfs(vertex):
        stack = [vertex]
        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                for neighbor in graph[v]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    for vertex in range(1, n + 1):
        if not visited[vertex]:
            components += 1
            dfs(vertex)

    return components


N = int(input())
graph = {i: [] for i in range(1, N + 1)}

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    graph[i] = line[1:]

print(count_connected_components(graph, N))
