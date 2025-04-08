import math
import random


def extract_coordinates(grid):
    nodes = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 5:
                nodes.insert(0, (x, y))
            elif grid[y][x] == 2:
                nodes.append((x, y))
    return nodes


def calculate_distances(nodes):
    """Calculate distances between nodes. Not used"""
    n = len(nodes)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = math.sqrt((nodes[i][0] - nodes[j][0])**2 + (nodes[i][1] - nodes[j][1])**2)
    return distances


grid = [[0 for _ in range(1000)] for _ in range(800)]
grid[400][500] = 5
for _ in range(5):
    x = random.randint(0, 999)
    y = random.randint(0, 799)
    grid[y][x] = 2  #
nodes = extract_coordinates(grid)
distances = calculate_distances(nodes)


for row in distances:
    print(row)
