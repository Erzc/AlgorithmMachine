#Time complexity of O(log n)
#Efficient search algorithm for sorted arrays

#class BinarySearch:
#    def __init__(self): #Initialize object’s state


def binary_search(arr, target):
    low = 0
    high = len(arr)-1 #Start with the entire array as the search space
    #Keep track of which part of the array to search in

    while low <= high:
        #Reduce by half until the target element is found or the search space is empty
        mid = (low + high) // 2
        mid_val_guess = arr[mid]

        if mid_val_guess == target: #Found the target
            return mid
        elif mid_val_guess < target: #Guess too low
            low = mid + 1
        else: #Guess too high
            high = mid - 1

    return -1 #If target not found

# Example usage:
sorted_arr = [4, 9, 15, 23, 36, 39, 45, 51, 68, 73, 75, 101, 124, 146, 178]
target_num = 75
result = binary_search(sorted_arr, target_num)

if result == -1:
    print(f"Sorry, your number {target_num} was not found in the array.")
else:
    print(f"Your number {target_num} was found at index {result}.")