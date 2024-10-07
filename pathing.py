import graph_data
import global_game_data
from numpy import random
import numpy as np
import config_data

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
    print(f"neighbors: {neighbors} type: {type(neighbors)}")
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
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

# def get_randomly_generated_path():
#     index1 = random.randint(0, len(graph_data.graph_data) - 1)
#     index2 = graph_data.graph_data[index1][random.randint(0, len(graph_data.graph_data[index1])-1)]
#     return [index1, index2]
