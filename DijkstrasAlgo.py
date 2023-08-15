#Dijkstras algorithm assumes non-negative edge weights

import heapq

#class DijkstraAlgo:
#    def __init__(self): #Initialize objects state


def find_shortest_distance(graph, start, final):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {}
    priority_queue = [(0, start)]

    while priority_queue:
        #Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)





#Passes graph and a starting vertex, returns dictionary with the shortest distances from starting vertex to all other vertices
#shortest_distance = find_shortest_distance(graph, 'A')
#print("Fastest route from A:")
#print(shortest_distance)