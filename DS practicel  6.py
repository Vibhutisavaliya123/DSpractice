P6#WAP to sort a list of elements. Give user the
option to perform sorting using Insertion sort,
Bubble sort or Selection sort.#

Code:Insertion sort

for i in range (Len(list_students_rolls)):
    min_val_index =I
for i in range (I+1,Len(list_students_rolls)):
    if list_students_rolls[min_Val_index] > list_students_roll[j]:
    min_Val_index =j
List_students_rolls[i],list_students_rollslist[min_Val_index] =
 list_students_roll[min_val_index],
list_students_rolls[i] 


Code : selection sort

def Selection(arr,n): 
    for i in range(n): 
        min_index = i 
        min_str = arr[i] 
     for j in range(i+1,n):
        if min_str> arr
           min_str = arr[j]
            min_index = j 
        if min_index !1
           temp = arr[i] 
           arr[i] = arr[min_index] 
           arr[min_index] = temp 
               return arr 
arr = ["GeeksforGeeks", "Practice.GeeksforGeeks", "GeeksQuiz"] 
print("Given array is") 
for i in range(len(arr)): 
 print(i,":",arr[i]) 

  

print("\nSorted array is") 

for i in range(len(Selection(arr,len(arr)))): 

    print(i,":",Selection(arr,len(arr))[i]) 

Code:Bubble sort

def bubbleSort(arr): 
    n = len(arr) 
for i in range(n-1):
for j in range(0, n-i-1): 
   if arr[j] > arr[j+1] : 
   arr[j], arr[j+1] = arr[j+1], arr[j] 
arr = [64, 34, 25, 12, 22, 11, 90] 

  
bubbleSort(arr) 

  

print ("Sorted array is:") 

for i in range(len(arr)): 

    print ("%d" %arr[i]),  





  










