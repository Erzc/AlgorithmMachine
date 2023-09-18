class SelectionSort:
    def __init__(self): #Initialize object’s state


        def findSmallest(arr):
            smallest = arr[0]
            smallest_index = 0
            for i in range(1, len(arr)):
                if arr[i] < smallest:
                    smallest = arr[i]
                    smallest_index = i
            return smallest_index


        def selectionSort(arr): #Sort array
            newArr = []
            for i in range(len(arr)):
                smallest = findSmallest(arr) #Find smallest element in array
                newArr.append(arr.pop(smallest)) #Then add to new array
            return newArr


        print(selectionSort([4, 7, 3, 5, 9, 2, 6, 3]))