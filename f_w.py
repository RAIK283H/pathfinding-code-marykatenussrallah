import graph
import graph_data
import math
import global_game_data

def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    dist = [[math.inf] * n for i in range(n)]
    parent = [[None] * n for i in range(n)]

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
        return None
    path = []
    while end is not None:
        path.append(end)
        end = parent[start][end]
    return path[::-1]

def adjacency_list_to_matrix(graph):
    n = len(graph)
    matrix = [[math.inf] * n for i in range(n)]
    for i, (coords, neighbors) in enumerate(graph):
        for neighbor in neighbors:
            matrix[i][neighbor] = 1
        matrix[i][i] = 0
    return matrix

import math

def get_floyd_warshall_full_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(curr_graph) - 1

    graph_matrix = adjacency_list_to_matrix(curr_graph)

    dist, parent = floyd_warshall(graph_matrix)

    path_to_target = reconstruct_path(parent, start_node, target_node)
    assert path_to_target is not None, f"Error: path_to_target doesn't exist"

    path_to_end = reconstruct_path(parent, target_node, end_node)
    assert path_to_end is not None, f"Error: path:_to_end doesn't exist"

    full_path = path_to_target[:-1] + path_to_end

    validate_full_path(full_path, curr_graph)

    return full_path


def validate_full_path(path, graph):
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        assert next_node in graph[current_node][1], f"Edge missing between {current_node} and {next_node}"



# NEW
# class FloydWarshallPathfinder:
#     def __init__(self, graph):
#         self.graph = graph
#         self.num_nodes = len(graph)
#         self.dist = [[float('inf')] * self.num_nodes for i in range(self.num_nodes)]
#         self.next_node = [[-1] * self.num_nodes for i in range(self.num_nodes)]
#         self._initialize()

#     def _initialize(self):
#         for i in range(self.num_nodes):
#             self.dist[i][i] = 0
#             for neighbor in self.graph[i][1]:
#                 self.dist[i][neighbor] = 1
#                 self.next_node[i][neighbor] = neighbor

#     def compute_shortest_paths(self):
#         for k in range(self.num_nodes):
#             for i in range(self.num_nodes):
#                 for j in range(self.num_nodes):
#                     if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
#                         self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
#                         self.next_node[i][j] = self.next_node[i][k]

#     def reconstruct_path(self, start, end):
#         if self.next_node[start][end] == -1:
#             return []  
#         path = [start]
#         while start != end:
#             start = self.next_node[start][end]
#             path.append(start)
#         return path

#     def get_path(self, start, target, end):
#         self.compute_shortest_paths()

#         start_to_target = self.reconstruct_path(start, target)
#         self.validate_path_segment(start_to_target, start, target)

#         target_to_end = self.reconstruct_path(target, end)
#         self.validate_path_segment(target_to_end, target, end)

#         full_path = self.combine_paths(start_to_target, target_to_end)
#         return full_path

#     def validate_path_segment(self, path, expected_start, expected_end):
#         assert path[0] == expected_start, f"Path does not start at the expected node {expected_start}"
#         assert path[-1] == expected_end, f"Path does not end at the expected node {expected_end}"

#     def combine_paths(self, path1, path2):
#         combined_path = path1[:-1] + path2
#         for i in range(len(combined_path) - 1):
#             current_node = combined_path[i]
#             next_node = combined_path[i + 1]
#             assert next_node in self.graph[current_node][1], f"Edge missing between {current_node} and {next_node}"
#         return combined_path


# def get_floyd_warshall_path():
#     curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
#     start_node = 0
#     target_node = global_game_data.target_node[global_game_data.current_graph_index]
#     end_node = len(curr_graph) - 1

#     fw_pathfinder = FloydWarshallPathfinder(curr_graph)
#     floyd_warshall_path = fw_pathfinder.get_path(start_node, target_node, end_node)

#     return floyd_warshall_path

