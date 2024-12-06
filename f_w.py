import graph
import graph_data
import math

def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    dist = [[math.inf] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph_matrix[i][j] != 0:
                dist[i][j] = graph_matrix[i][j]
                parent[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]

    return dist, parent

def reconstruct_path(parent, start, end):
    if parent[start][end] is None:
        return None  # No path
    path = []
    while end is not None:
        path.append(end)
        end = parent[start][end]
    return path[::-1]

def adjacency_list_to_matrix(graph):
    n = len(graph)
    matrix = [[math.inf] * n for _ in range(n)]
    for i, (coords, neighbors) in enumerate(graph):
        for neighbor in neighbors:
            matrix[i][neighbor] = 1  # Replace with actual weights if available
        matrix[i][i] = 0  # Distance to self is 0
    return matrix
