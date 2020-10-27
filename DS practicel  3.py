#P3. Implement the following for stack.
 A) Perform stack operations using array implementation
        
  Code:
stack = [] 

stack.append('a') 

stack.append('b') 

stack.append('c') 

  

print('Initial stack') 

print(stack)

print('\nElements poped from stack:') 

print(stack.pop()) 

print(stack.pop()) 

print(stack.pop()) 

  

print('\nStack after elements are poped:') 

print(stack) 

B) Implement tower of hanoi

Code:
def TowerOfHanoi(n , source, destination, auxiliary): 

    if n==1: 

        print "Move disk 1 from source",source,"to destination",destination 

        return

    TowerOfHanoi(n-1, source, auxiliary, destination) 

    print "Move disk",n,"from source",source,"to destination",destination 

    TowerOfHanoi(n-1, auxiliary, destination, source) 

          
# Driver code 

n = 4

TowerOfHanoi(n,'A','B','C')  

C) wap to scan a polyano mail using linked list
and add two polynomial
struct Node 
Code:-
def add(A, B, m, n): 

  

    size = max(m, n); 

    sum = [0 for i in range(size)] 

    for i in range(0, m, 1): 

        sum[i] = A[i] 
 

    for i in range(n): 

        sum[i] += B[i] 

  

    return sum 

def printPoly(poly, n): 

    for i in range(n): 

        print(poly[i], end = "") 

        if (i != 0): 

            print("x^", i, end = "") 

        if (i != n - 1): 

            print(" + ", end = "") 

  
# Driver Code 

if __name__ == '__main__': 

      

    # The following array represents 

    # polynomial 5 + 10x^2 + 6x^3 

    A = [5, 0, 10, 6] 

  

    # The following array represents 

    # polynomial 1 + 2x + 4x^2 

    B = [1, 2, 4] 

    m = len(A) 

    n = len(B) 

  

    print("First polynomial is") 

    printPoly(A, m) 

    print("\n", end = "") 

    print("Second polynomial is") 

    printPoly(B, n) 

    print("\n", end = "") 

    sum = add(A, B, m, n) 

    size = max(m, n) 

  

    print("sum polynomial is") 

    printPoly(sum, size) 


     


D)wap to calculate factorial and to complete the
Factors of give no using recursion and using iteration

# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num)) un









