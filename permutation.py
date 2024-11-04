from itertools import permutations

def generate_permutations(n):
    # excludes start and end nodes
    perm = list(range(1, n))
    # this makes all of the elements in the list point left to begin
    direction = [-1] * (n-1)

    # allows function to access the permutation and still go back into function here
    yield perm[:]
    while True:
        mobile = find_largest_mobile(perm, direction)
        # if mobile isn't found, leave loop
        if mobile == -1:
            break
        swap_elements(perm, mobile, mobile + direction[mobile])
        reverse_larger_elements(perm, direction, perm[mobile])
        # allows function to access the permutation and still go back into function here
        yield perm[:]

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
    exit_node = len(graph) -1
    # checks to see if the first node is adjacent to exit node and returns if it's true or not
    return path[-1] in graph[exit_node][1]
