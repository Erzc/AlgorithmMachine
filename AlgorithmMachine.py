# Programmer: Eric N
# Purpose: Demonstrate use of different algorithms
# Python version 3.11

# import BinarySearch.py file
#from BinarySearch import BinarySearch as binarySearch


#--------------------Main---------

#Loop until user quits
while True:
    #Try except statement to handle float value exception
    try:
        #Ask for user algorithm/problem
        print("stories go here")
        user_story = input("\nPlease select an algorithm to work on (enter an integer): ")

        #Match-case statement, instantiate class object depending on answer
        def match_result(x):
            match x:
                case '1':
                    return ""
                case '2':
                    return ""
                case '3':
                    return ""
                case '4':
                    return ""
                case '5':
                    return ""
                case '6':
                    return ""
                case '7':
                    return ""
                case '8':
                    return ""
                case _:
                    return "0"   #Default case
        
        result_story = match_result(user_story)

    #Exception handling
    except TypeError :
        print ("Error! Wrong data type.")
    except NameError:
        print ("Error! Data name unknown.")
    except Exception as e:
        print ("Error! Something went wrong...", e)
    
    again = input("\nDo another story (y/n)?")
    if again == "n":
        break


print("You exited the program, goodbye!")