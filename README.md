# Pathfinding Starter Code
1. In my get_random_path() algorithm, I start by getting the current graph we're using from the global_game_data class' current_graph_index function and then using that as the index for the graph_data.graph_data (gets me the actual graph from the graph_data class). Then I assign the currentStartNode to be 0 since the graphs all start at the zeroth position. I make currentEndNode the last node in the graph since we end at the last node in the graph. I make currTargetNodeIndex by getting the targetNodeIndex from global_graph_data. Then I make a list called randomPath and append currStartNode since we'll always be starting there. I set neighborsIndex equal to currStartNode and use it to get a list of the neighbors of the first node. Then I enter a while loop that will end once currEndNode and currTargetNode are in the randomPath. I set nextNode equal to a random choice from neighbors and then turn it into an int. I next append it to randomPath. Then i check to see if neighborIndex is less than the lenght of currGraph and if it is, i set neighborIndex equal to nextNode and get neighbors from this node. Then we repeat the while loop until currEndNode and currTargetNode are both in randomPath. We return randomPath.

2. In my display_nodes_visited() function, all of the nodes in the graph are looked at and then the ones that are visited are counted. This counts if it goes back to a node (like the node will be counted twice). This number is then displayed on the scoreboard.