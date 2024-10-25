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
    visited = set([curr_node_index])
    prev_node = {curr_node_index: None}
    while dfs_stack:
         node = dfs_stack.pop()
         if node == target_node_index:
              break
         for neighbor in reversed(curr_graph[node][1]):
              if neighbor not in visited:
                visited.add(neighbor)
                dfs_stack.append(neighbor)
                prev_node[neighbor] = node

    dfs_path = []
    node = target_node_index
    while node is not None:
         dfs_path.append(node)
         node = prev_node.get(node)
    dfs_path.reverse()
    assert dfs_path[-1] == target_node_index, "Error: DFS path to the target doesn't end with the target"
    dfs_stack = deque([target_node_index])
    visited = set([target_node_index])
    prev_node = {target_node_index: None}
    while dfs_stack:
         node = dfs_stack.pop()
         if node == end_node_index:
              break
         for neighbor in reversed(curr_graph[node][1]):
              if neighbor not in visited:
                visited.add(neighbor)
                dfs_stack.append(neighbor)
                prev_node[neighbor] = node
    dfs_path_to_end = []
    node = end_node_index
    while node is not None:
         dfs_path_to_end.append(node)
         node = prev_node.get(node)
    dfs_path_to_end.reverse()
    assert dfs_path_to_end[-1] == end_node_index, "Error: DFS path doesn't end at the end node"
    for path in dfs_path_to_end[1:]:
         dfs_path.append(path)
    for i in range(len(dfs_path) - 1):
        current_node = dfs_path[i]
        next_node = dfs_path[i+1]
        assert next_node in curr_graph[current_node][1], f"Error: no edge between {current_node} and {next_node} in DFS path."
    return dfs_path


def get_bfs_path():
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    curr_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    end_node_index = len(curr_graph)-1
    bfs_queue = deque([curr_node_index])
    visited = set([curr_node_index])
    prev_node = {curr_node_index: None}
    while bfs_queue:
         curr_node = bfs_queue.popleft()
         if curr_node == target_node_index:
              break
         for neighbor in curr_graph[curr_node][1]:
              if neighbor not in visited:
                   visited.add(neighbor)
                   bfs_queue.append(neighbor)
                   prev_node[neighbor] = curr_node
    bfs_path = []
    node = target_node_index
    while node is not None:
         bfs_path.append(node)
         node = prev_node.get(node)
    bfs_path.reverse()
    assert target_node_index in bfs_path, "Error: did not pass postcondition. Target node not in BFS path"
    bfs_queue = deque([target_node_index])
    visited = set([target_node_index])
    prev_node = {target_node_index: None}

    while bfs_queue:
         curr_node = bfs_queue.popleft()
         if curr_node == end_node_index:
              break
         for neighbor in curr_graph[curr_node][1]:
              if neighbor not in visited:
                   visited.add(neighbor)
                   bfs_queue.append(neighbor)
                   prev_node[neighbor] = curr_node
    target_to_exit_path = []
    node = end_node_index
    while node is not None:
         target_to_exit_path.append(node)
         node = prev_node.get(node)
    target_to_exit_path.reverse()
    for path in target_to_exit_path[1:]:
         bfs_path.append(path)
    assert bfs_path[-1] == end_node_index, "Error: did not pass postcondition. BFS path doesn't end with the end node"
    for i in range(len(bfs_path) - 1):
         assert bfs_path[i+1] in curr_graph[bfs_path[i]][1], f"Error: didn't pass postcondition. Not all connected nodes in BFS path are direct neighbors"
    return bfs_path


def get_dijkstra_path():
    return [1,2]


