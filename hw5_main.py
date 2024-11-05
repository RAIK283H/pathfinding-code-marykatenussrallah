import graph_data
import permutation
from itertools import permutations


# graph_index = 1
# graph = graph_data.graph_data[graph_index]
# n = len(graph)

# # goes through all the graphs in the graph_data array in the graph data class
# for graph in graph_data.graph_data:
#     n = len(graph)
#     # generates the permutaions for each graph
#     for perm in permutation.generate_permutations(n):
#         path = [0] + perm + [n-1]
#         # checks if there's a hamiltonian cycle in each graph
#         if permutation.check_hamiltonian_cycle(graph, path):
#             print(f"Hamiltonitan cycle found: {path}")
#         else:
#             print(f"Hamiltonian cycle found: False")

# # checks for a hamiltonian cycle but we know it'll be true because we are only checking the one graph that was hard-coded as a hamiltonian cycle
# graph_index = 0
# graph = graph_data.hamiltonian_cycle
# n = len(graph)
# for perm in permutation.generate_permutations(n):
#     path = [0] + perm + [n-1]
#     if permutation.check_hamiltonian_cycle(graph, path):
#         print(f"Hamiltonitan cycle found: {path}")
#     else:
#         print(f"Hamiltonian cycle found: {permutation.check_hamiltonian_cycle(graph, path)} path: {path}")

for graph in graph_data.graph_data:
    hamiltonian_cycles = []
    optimal_cycles = []
    shortest_distance = 100000000

    for perm in permutation.generate_permutations(len(graph)):
        path = [0] + perm + [len(graph) - 1]
        if permutation.check_hamiltonian_cycle(graph, path):
            distance = permutation.calculate_distance(graph, path)
            print(f"Hamiltonitan cycle found: {path}")
            if distance < shortest_distance:
                shortest_distance = distance
                optimal_cycles = [path]
            elif distance == shortest_distance:
                optimal_cycles.append(path)
        else:
                print(f"Hamiltonian cycle found: False")
    print(f"Optimal Hamiltonian cycles: {optimal_cycles}")
