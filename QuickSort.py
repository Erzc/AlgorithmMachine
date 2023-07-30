#divide-and-conquer
#Average: O(log n)
#Worst case: O(n)

#class QuickSort:
#    def __init__(self): #Initialize object’s state


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot] #Sub-array of all elements less than the pivot
        equal = [x for x in arr if x == pivot] #Equal
        greater = [x for x in arr if x > pivot] #Greater

        return quicksort(less) + equal + quicksort(greater)

#Test quicksort function
arr = [4, 6, 3, 7, 1, 9, 2, 5]
sorted_arr = quicksort(arr)
print(f"Here's the sorted array: {sorted_arr}.")