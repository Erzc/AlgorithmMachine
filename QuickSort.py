#divide-and-conquer
#Average: O(log n)
#Worst case: O(n)

class QuickSort:
    def __init__(self): #Initialize object’s state


        def quicksort(arr):
            if len(arr) < 2: #If the array is less than 2 then it is already sorted
                return arr
            else: #Sort the initial array into 3 sub-arrays, then call itself in the return statement to further refine
                pivot = arr[len(arr) // 2] #Find the middle element of array
                less = [x for x in arr if x < pivot] #Sub-array of all elements less than the pivot
                equal = [x for x in arr if x == pivot] #Equal
                greater = [x for x in arr if x > pivot] #Greater

                return quicksort(less) + equal + quicksort(greater) #Recursively calls itself using the new less/greater arrays
            
        #Display story to user:
        story = '''
        \nThis algorithm sorts an array of integers from least to greatest using a pivot
        number and three sub-arrays: less than, equal to, or greater than. Then it calls itself
        recursively using the sub-arrays and returns the final concatenated sorted array.
        '''

        print(story)

        #Initialize array and call quicksort function
        arr = [4, 6, 3, 7, 1, 9, 2, 5, 2]
        sorted_arr = quicksort(arr)
        print(f"Here's the sorted array: {sorted_arr}.")