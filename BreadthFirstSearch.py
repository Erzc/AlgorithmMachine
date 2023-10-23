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

        def check_names(last_l, person_name):
            return person_name[-1] == last_l

        def search(last_letter, name):
            names_with_y = []
            search_queue = deque() #Create a new queue
            search_queue += graph[name] #Add the neighbors of the starting person
            searched = [] #Keep track of visited nodes

            while search_queue: #While queue is not empty
                person = search_queue.popleft()  #Get front node from the queue
                if not person in searched: #Only search if person not already searched
                    if check_names(last_letter, person):
                        names_with_y.append(person)
                    search_queue.extend(graph[person])
                    searched.append(person) #Mark person as searched

            return names_with_y

        #Display story to user:
        story = '''
        Here is a full list of neighbors, presented as a graph:

        "Abby": ["Emile"],
        "Emile": ["Mike", "Ron"],
        "Mike": [],
        "Harry": ["Lewis"],
        "Lewis": ["Carl"],
        "Poe": ["Harry"],
        "Ron": ["Poe", "Emile"],
        "Carl": ["Abby", "Harry"]

        This algorithm finds and displays all names that end with a specific character.\n
        '''

        print(story)

        while True:
            last_let = input("Please enter a single character: ")
            
            #Verify single character and is an alphabet letter
            if len(last_let) == 1 and last_let.isalpha():
                break
            else:
                print("Error! Please enter a single character.")

        #Start searching from Abby
        names_ending_with_y = search(last_let,"Abby")

        #Print all names if names found
        if names_ending_with_y:
            print("\nNames that end with {}".format(last_let))
            for name in names_ending_with_y:
                print(name)
        else:
            print("\nNo names end with {}".format(last_let))