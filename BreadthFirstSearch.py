#The BFS algorithm explores all reachable nodes and edges, so the time complexity grows linearly with the size of the input graph
#O(V + E)
    #V - vertices (nodes) i.e. people
    #E - edges i.e. relationships


from collections import deque

class BreadthFirstSearch:
    def __init__(self): #Initialize object’s state

        #Dictionary to represent the graph
        graph = {
            "Abby": ["Emile"],
            "Emile": ["Mike", "Ron"],
            "Mike": [],
            "Harry": ["Lewis"],
            "Lewis": ["Carl"],
            "Poe": ["Harry"],
            "Ron": ["Poe", "Emile"],
            "Carl": ["Abby", "Harry"]
        }

        def check_names(person_name):
            return person_name[-1] == 'y'

        def search(name):
            names_with_y = []
            search_queue = deque() #Create a new queue
            search_queue += graph[name] #Add the neighbors of the starting person
            searched = [] #Keep track of visited nodes

            while search_queue: #While queue is not empty
                person = search_queue.popleft()  #Get front node from the queue
                if not person in searched: #Only search if person not already searched
                    if check_names(person):
                        names_with_y.append(person)
                    search_queue.extend(graph[person])
                    searched.append(person) #Mark person as searched

            return names_with_y

        #Display story to user:
        #
        #

        #Start searching from Abby
        names_ending_with_y = search("Abby")

        #Print all names if names found
        if names_ending_with_y:
            print("Names that end with 'y':")
            for name in names_ending_with_y:
                print(name)
        else:
            print("No names end with 'y'.")