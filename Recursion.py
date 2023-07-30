#class Recursion:
#    def __init__(self): #Initialize object’s state

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

#Using the factorial function
result = fact(20)
print(f"Factorial of {number} is: {result}")
