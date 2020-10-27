P6#WAP to sort a list of elements. Give user the
option to perform sorting using Insertion sort,
Bubble sort or Selection sort.#

Code:Insertion sort

def insertionSort(arr): 

  

    # Traverse through 1 to len(arr) 

    for i in range(1, len(arr)): 

  

        key = arr[i] 

  

        # Move elements of arr[0..i-1], that are 

        # greater than key, to one position ahead 

        # of their current position 

        j = i-1

        while j >=0 and key < arr[j] : 

                arr[j+1] = arr[j] 

                j -= 1

        arr[j+1] = key 

  

  
# Driver code to test above 

arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 

print ("Sorted array is:") 

for i in range(len(arr)): 

    print ("%d" %arr[i]) 


Code : selection sort
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)


  



Code:Bubble sort

def bubbleSort(arr): 

    n = len(arr)

    # Traverse through all array elements 

    for i in range(n-1): 
      
        for j in range(0, n-i-1): 
         

            if arr[j] > arr[j+1] : 

                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90] 

  
bubbleSort(arr) 

  

print ("Sorted array is:") 

for i in range(len(arr)): 

    print ("%d" %arr[i]),






  










