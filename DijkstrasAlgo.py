#Dijkstras algorithm assumes non-negative edge weights
#Time complexity of Dijkstra's algorithm with a binary heap (priority queue) is: 
#O((V + E) log V)
    #V = vertices (nodes) i.e. letters
    #E = edges i.e. relationships/weights

import heapq

class DijkstraAlgo:
    def __init__(self): #Initialize objects state


        def find_shortest_distance(graph, start, final):
            
            #Initialize distances dictionary
            distances = {}
            for node in graph:
                distances[node] = float('inf')

            distances[start] = 0
            #Dictionary keeps track of the previous node
            predecessors = {}
            #Initialize priority queue (min-heap) with single tuple representing the starting node and its initial distance
            priority_queue = [(0, start)]

            while priority_queue:
                #VERBOSE - Remove and retrieve the smallest distance from the priority queue
                #Retrieve the node with the smallest distance from the priority queue
                smallest_distance_node = heapq.heappop(priority_queue)
                #Separate the extracted tuple into its components
                current_distance = smallest_distance_node[0]
                current_node = smallest_distance_node[1]

                #If 'E' node is reached, end while loop
                if current_node == final:
                    break

                #If current distance is greater than distance value stored in dictionary, skip current loop iteration
                if current_distance > distances[current_node]:
                    continue

                #Retrieve the current node's neighbors and their corresponding edge weights
                #.items() returns an iterable of key-value pairs (items) from the dictionary
                neighbor_weight_pairs = graph[current_node].items()
                for neighbor_weight_pair in neighbor_weight_pairs:
                    neighbor = neighbor_weight_pair[0]
                    weight = neighbor_weight_pair[1]

                    #calculate new potential distance from starting node to a neighboring node
                    distance = current_distance + weight

                    #check if the new distance is less than the current stored distance for that node
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        #The shortest path to the neighbor node involves first traversing the current node
                        predecessors[neighbor] = current_node
                        #CONCISE - Push nodes into the priority queue while maintaining the heap property
                        heapq.heappush(priority_queue, (distance, neighbor))

            #Reconstruct the shortest path from starting to final node
            path = []
            while final:
                #Add the current node to the start of the path
                path.insert(0, final)
                #Update the final node to its predecessor node
                final = predecessors.get(final)

            return path

        #Graph
        graph = {
            'A': {'B': 4, 'C': 7},
            'B': {'A': 5, 'B': 3, 'C': 3},
            'C': {'A': 7, 'B': 2, 'E': 8},
            'E': {'B': 3, 'C': 5}
        }

        start_node = 'A'
        final_node = 'E'
        #Call Dijkstra's algorithm function, passing the graph, start, and end nodes
        shortest_path = find_shortest_distance(graph, start_node, final_node)
        #Display the shortest path to the user
        print("Shortest path:", shortest_path)