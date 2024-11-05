from itertools import permutations
import itertools
import math

def generate_permutations(n):
    # excludes start and end nodes
    perm = list(range(1, n-1))
    # this makes all of the elements in the list point left to begin
    direction = [-1] * (n-1)
    all_permutations = [perm[:]]

    while True:
        mobile = find_largest_mobile(perm, direction)
        # if mobile isn't found, leave loop
        if mobile == -1:
            break
        swap_elements(perm, mobile, mobile + direction[mobile])
        reverse_larger_elements(perm, direction, perm[mobile])
        # allows function to access the permutation and still go back into function here
        all_permutations.append(perm[:])
    return all_permutations

def find_largest_mobile(perm, direction):
    # sets mobile to equal an element not in the list
    mobile = -1
    # goes through perm and sees if elements are facing left and are greater than the element to their left
    # OR if they're facing right and are in the list and are greater than the element to their right
    for i in range(len(perm)):
        if ((direction[i] == -1 and i > 0 and perm[i] > perm[i-1]) or (direction[i] == 1 and i < len(perm) - 1 and perm[i] > perm[i + 1])):
            # if mobile is still -1 or the element we're looking at is greater than the element at mobile currently, set mobile equal to the element we're looking at
            if mobile == -1 or perm[i] > perm[mobile]:
                mobile = i
    return mobile

def swap_elements(perm, i, j):
    # swaps two elements in perm
    perm[i], perm[j] = perm[j], perm[i]

def reverse_larger_elements(perm, direction, mobile_value):
    # goes through every element in perm
    for i in range(len(perm)):
        # checks to see if the element we're looking at is greater than the mobile vaule, if it is change its direction
        if perm[i] > mobile_value:
            direction[i] *= -1

def check_hamiltonian_cycle(graph, path):
    # goes through all elements in path
    for i in range(len(path) - 1):
        # assigns current_node to the one we're looking at and next_node to the one to the right of current_node
        current_node, next_node = path[i], path[i + 1]
        # checks to see if next_node is adjacent to current_node, if it's not, returns false
        if next_node not in graph[current_node][1]:
            return False
    # sets exit_node equal to the last node in the graph
    exit_node = len(graph)-1
    return path[exit_node] in graph[0][1]

def calculate_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        node_a, node_b = path[i], path[i+1]
        x1, y1 = graph[node_a][0]
        x2, y2 = graph[node_b][0]
        distance += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def find_optimal_hamiltonian_cycles(graph):
    n = len(graph)
    min_distance = float('inf')
    optimal_cycles = []
    for perm in itertools.permutations(range(1, n-1)):
        path = [0] + list(perm) + [n-1]
        if check_hamiltonian_cycle(graph, path):
            dist = calculate_distance(graph, path)
            if dist < min_distance:
                min_distance = dist
                optimal_cycles = [path]
            elif dist == min_distance:
                optimal_cycles.append(path)
    return optimal_cycles, min_distance

def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[j] not in graph[nodes[i]][1]:
                return False
    return True

def find_largest_clique(graph):
    n = len(graph)
    max_clique = []
    nodes = list(range(1, n-1))
    for subset_size in range(len(nodes), 0, -1):
        for subset in itertools.combinations(nodes, subset_size):
            if is_clique(graph, subset):
                if len(subset) > len(max_clique):
                    max_clique = subset
    return max_clique
                                     
