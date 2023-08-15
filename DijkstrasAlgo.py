#Dijkstras algorithm assumes non-negative edge weights

import heapq

#class DijkstraAlgo:
#    def __init__(self): #Initialize objects state


#______
#Graph

graph = {
    'Start': {'B': 5, 'C': 6},
    'A': {'B': 4, 'C': 7},
    'B': {'A': 5, 'C': 3, 'D': 3},
    'C': {'A': 7, 'B': 2, 'Final': 8},
    'D': {'B': 3, 'C': 5},
    'Final': {}
}

costs_table =  {
    'Start': 7,
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'Final': float('inf')
}

parents = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'Final': None
}

#Array to keep track of all processeed nodes
processed = []


def find_shortest_distance(graph):
    lowest_cost = float("inf")
    lowest_cost_node = None
    #For loop to go through each node
    for node in costs_table:
        cost = costs_table[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_shortest_distance(costs_table)

while node is not None:
    cost = costs_table[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs_table[n] > new_cost:
            costs_table[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_shortest_distance(costs_table)

    print("Updated costs table:", costs_table)
    print("Updated parents:", parents)
    print("Processed nodes:", processed)

print("Fastest route from A:")
print(node)





#Passes graph and a starting vertex, returns dictionary with the shortest distances from starting vertex to all other vertices
#shortest_distance = find_shortest_distance(graph, 'A')
#print("Fastest route from A:")
#print(shortest_distance)