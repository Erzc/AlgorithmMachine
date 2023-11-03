class Recursion:
    def __init__(self): #Initialize object’s state

        def fact(n):
            if n == 1:
                #Base case
                return 1
            else:
                #Recursion case: Function calls itself with the argument n-1 until it reaches the base case
                return n * fact(n-1)

        #Display story to user:
        story = '''
        \nThis algorithm calculates the factorial of a positive integer using recursion (calling itself within a function).

        '''

        print(story)

            #Loop to get and verify user's integer
        while True:
            try:
                user_num = int(input("Please enter an integer for the purpose of calculating its factorial: "))
                break  #Exit loop if conversion succeeds
            except ValueError:
                print("Error! Please enter an integer.")

        #Call the factorial function
        result = fact(user_num)
        print(f"\nThe factorial of {user_num} is: {result}")
