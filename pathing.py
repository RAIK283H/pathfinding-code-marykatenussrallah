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
    currGraphIndex = graph_data.graph_data.index(currGraph)
    currGraphLen = len(currGraph)
    print(f"currGraphIndex: {currGraphIndex} type: {type(currGraphIndex)}")
    print(f"length of Index: {len(currGraph)}")
    # print(f"currGraph: {currGraph} type: {type(currGraph)}")
    currStartNode = currGraph[0]
    # print(f"currStartNode: {currStartNode} type: {type(currStartNode)}")
    currEndNode = currGraph[len(currGraph)-1]
    # print(f"currEndNode: {currEndNode} type: {type(currEndNode)}")
    currTargetNodeIndex = global_game_data.target_node[global_game_data.current_graph_index]
    currTargetNode = currGraph[currTargetNodeIndex]
    # print(f"currTargetNode: {currTargetNode} type: {type(currTargetNode)}")
    randomPath = []
    randomPath.append(currStartNode)
    targetNodeFound = False
    while currEndNode not in randomPath:
        # tempList = graph_data.graph_data
        # currNodeIndex = currGraph[]
        neighbors = currGraph[1]
        print(f"neighbors: {neighbors} type: {type(neighbors)}")
        # nextNode = 
    return [1,2]


# def get_random_path():
#     currGraph = graph_data.graph_data[global_game_data.current_graph_index]
#     currStart = currGraph[0][0]
#     currEnd = currGraph[len(currGraph)-1]
#     currTarget = global_game_data.target_node[global_game_data.current_graph_index]
#     currTargetPosition = currGraph[currTarget][0]
#     # make a path from currStart to currTarget
#     currPosition = currStart
#     path = [currStart]
#     if currTarget not in path:
#         while currPosition != currTarget:
#             currPositionIndex = currGraph[0].index(currPosition)
#             neighbors = currGraph[currPositionIndex][1]
#             nextPosition = random.choice(neighbors)
#             if isinstance(nextPosition, (list, np.integer)):
#                 nextPosition = int(nextPosition)
#             if nextPosition not in path:
#                 path.append(nextPosition)
#                 currPosition = nextPosition
#     else:
#         while currPosition != currEnd:
#             currPositionIndex = currGraph[0].index(currPosition)
#             neighbors = currGraph[currPositionIndex][1]
#             nextPosition = random.choice(neighbors)
#             if isinstance(nextPosition, (list, np.integer)):
#                 nextPosition = int(nextPosition)
#             if nextPosition not in path:
#                 path.append(nextPosition)
#                 currPosition = nextPosition
#     return path


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
