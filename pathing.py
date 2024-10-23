import graph_data
import global_game_data
from numpy import random
import numpy as np
from collections import deque


def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

def get_random_path():
    currGraph = graph_data.graph_data[global_game_data.current_graph_index]
    currStartNode = 0
    currEndNode = len(currGraph)-1
    currTargetNodeIndex = global_game_data.target_node[global_game_data.current_graph_index]
    randomPath = []
    randomPath.append(currStartNode)
    neighborIndex = currStartNode
    neighbors = currGraph[neighborIndex][1]
    while currEndNode not in randomPath or currTargetNodeIndex not in randomPath:
        nextNode = random.choice(neighbors)
        if isinstance(nextNode, (list, np.integer)):
                nextNode = int(nextNode)
        randomPath.append(nextNode)
        if neighborIndex < len(currGraph):
            neighborIndex = nextNode
            neighbors = currGraph[neighborIndex][1]
    return randomPath


def get_dfs_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    curr_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    end_node_index = len(curr_graph) - 1
    dfs_stack = deque([curr_node_index])
    visited = set()
    dfs_path = []
    while end_node_index not in dfs_stack or target_node_index not in dfs_stack:
         node = dfs_stack.pop()
         if node not in visited:
              visited.add(node)
              dfs_path.append(node)
              for neighbor in reversed(curr_graph[node][1]):
                   if neighbor not in visited:
                        dfs_stack.append(neighbor)
    dfs_path.append(end_node_index)
    assert dfs_path[-1] == end_node_index, "Error: DFS path doesn't end at the end node"
    # for i in range(len(dfs_path) - 1):
    #     assert dfs_path[i+1] in curr_graph[dfs_path[i][1]], f"Error: no edge between {dfs_path[i]} and {dfs_path[i+1]} in DFS path."
    return dfs_path


def get_bfs_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    curr_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    end_node_index = len(curr_graph)-1
    bfs_stack = deque([curr_node_index])
    visited = set()
    bfs_path = []
    while end_node_index not in bfs_stack or target_node_index not in bfs_stack:
        node = bfs_stack.popleft()
        if node == end_node_index:
            bfs_path.append(node)
            break
        if node not in visited:
            visited.add(node)
            bfs_path.append(node)
            for neighbor in curr_graph[node][1]:
                if neighbor not in visited:
                    bfs_stack.append(neighbor)
    # assert bfs_path[-1] == end_node_index, "Error: BFS path doesn't end at the end node"
    # for i in range(len(bfs_path) - 1):
    #     assert bfs_path[i+1] in curr_graph[bfs_path[i][1]], f"Error: no edge between {bfs_path[i]} and {bfs_path[i+1]} in BFS path."
    return bfs_path


def get_dijkstra_path():
    return [1,2]

# def get_randomly_generated_path():
#     index1 = random.randint(0, len(graph_data.graph_data) - 1)
#     index2 = graph_data.graph_data[index1][random.randint(0, len(graph_data.graph_data[index1])-1)]
#     return [index1, index2]
