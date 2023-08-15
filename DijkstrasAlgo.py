#Dijkstras algorithm assumes non-negative edge weights

import heapq

#class DijkstraAlgo:
#    def __init__(self): #Initialize objects state






#______
#Graph represented as an adjacency list
graph_costs = {
    'Start': 2,
    'A': 4,
    'B': 3,
    'C': 5,
    'Fin': 7
}

parents = {
    'A': "start",
    'B': "start",
    'Fin': None
}

#Array to keep track of all processeed nodes
processed = []


def find_shortest_distance(graph):
    lowest_cost = float("inf")
    lowest_cost_node = None
    #For loop to go through each node
    for node in graph_costs:
        cost = graph_costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_shortest_distance(graph_costs)

while node is not None:
    cost = graph_costs[node]
    neighbors = cost[node]
    for n in neighbors.key():
        new_cost = cost + neighbors[n]
        if graph_costs[n] > new_cost:
            graph_costs[n] = new_cost
            parents[n] = node

    processed.append[node]
    node = find_shortest_distance(node)

print("Fastest route from A:")
print(node)




#Passes graph and a starting vertex, returns dictionary with the shortest distances from starting vertex to all other vertices
#shortest_distance = find_shortest_distance(graph, 'A')
#print("Fastest route from A:")
#print(shortest_distance)