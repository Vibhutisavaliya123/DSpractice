P5##Write a program to search an element from a 
list. Give user the option to perform Linear
or Binary search. #

Code:linear

def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 
    return -1; 
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ]; 
x = 10; 
n = len(arr); 
result = search(arr, n, x) 
if(result == -1): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result);


Code binary:-
def binary_search(arr, low, high, x): 

  

    # Check base case 

    if high >= low: 

  

        mid = (high + low) // 2

  

        # If element is present at the middle itself 

        if arr[mid] == x: 

            return mid 

  

        # If element is smaller than mid, then it can only 

        # be present in left subarray 

        elif arr[mid] > x: 

            return binary_search(arr, low, mid - 1, x) 

  

        # Else the element can only be present in right subarray 

        else: 

            return binary_search(arr, mid + 1, high, x) 

  

    else: 

        # Element is not present in the array 

        return -1

  
# Test array 

arr = [ 2, 3, 4, 10, 40 ] 

x = 10

  
# Function call 

result = binary_search(arr, 0, len(arr)-1, x) 

  

if result != -1: 

    print("Element is present at index", str(result)) 

else: 

    print("Element is not present

