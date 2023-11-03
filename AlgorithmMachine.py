# Programmer: Eric N
# Purpose: Demonstrate use of different algorithms
# Python version 3.11

# import BinarySearch.py file
from BinarySearch import BinarySearch as binarySearch
from BreadthFirstSearch import BreadthFirstSearch as breadthFirstSearch
from DijkstrasAlgo import DijkstrasAlgo as dijkstrasAlgo
from GreedyAlgo import GreedyAlgo as greedyAlgo
from Recursion import Recursion as recursion
from SelectionSort import SelectionSort as selectionSort


#--------------------Main---------

#Loop until user quits
while True:

    #Display stories/choices
    choices = '''
    ALGORITHM CHOICES:
    1. Binary Search - Finds the index of a target number within a sorted array.
    2. Breadth First Search - Returns all names that end with a target character within a graph of neighbors.
    3. Dijkstras Algorithm - Retrieves the shortest path between two characters within a graph of neighbors.
    4. Greedy Algorithm - Finds the minimum number of coins needed to reach a target price.
    5. Recursion - 
    6. Selection Sort - 
    '''

    print(choices)

    #Try except statement to handle value exception
    try:
        #Ask user for algorithm/problem
        user_story = int(input("\nPlease select an algorithm (enter a number 1-6): \n"))
        if user_story < 1 or user_story > 6:
            raise ValueError("Your number must be between 1 and 6")
    except TypeError :
        print ("Error! Wrong data type.")
        continue
    except NameError:
        print ("Error! Data name unknown.")
        continue
    except Exception as e:
        print ("Error! Something went wrong...", e)
        continue

    #Match-case statement, instantiate class object depending on answer
    def match_result(y):
        match y:
            case 1:
                return binarySearch()
            case 2:
                return breadthFirstSearch()
            case 3:
                return dijkstrasAlgo()
            case 4:
                return greedyAlgo()
            case 5:
                return recursion()
            case 6:
                return selectionSort()
            case _:
                return "Error! Please enter a number 1-6."   #Default casea
    
    #Call function to run match case statement
    result_story = match_result(user_story)

    #Ask if user wants to do another
    again = input("\nDo another story (y/n)?").strip().lower()
    if again != "y":
        break


print("You exited the program, goodbye!")