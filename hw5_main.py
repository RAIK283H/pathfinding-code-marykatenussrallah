import graph_data
import permutation
from itertools import permutations


graph_index = 1
graph = graph_data.graph_data[graph_index]
n = len(graph)

for perm in permutation.generate_permutations(n):
    path = [0] + perm + [n-1]
    if permutation.check_hamiltonian_cycle(graph, path):
        print(f"Hamiltonitan cycle found: {path}")
    # else:
    #     print(f"Not Hamiltonian cycle {path}")

graph_index = 0
graph = graph_data.hamiltonian_cycle
n = len(graph)
for perm in permutation.generate_permutations(n):
    path = [0] + perm + [n-1]
    if permutation.check_hamiltonian_cycle(graph, path):
        print(f"Hamiltonitan cycle found: {path}")