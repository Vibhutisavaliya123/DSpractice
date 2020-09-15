#P1_A  Write a program to store the elements in
 1-D array and provide an option to perform
 the operations like searching, sorting,
 merging, reversing the elements.#


Code: searching
Def Binary_search(list value_, search,start,end):
    if start > end:
       return - 1
    mid = (start + end)//2
    if list_values[mid] == search:
       return mid
    if element < list_value[mid]:
       return binary_search(list_values,search,start,mid-1)
else:
       return binary_search(list_values,search,start,mid+1,end)




Code: sorting

def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)


Code: merging

def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)

Code:reversing

def Reverse(Number):  # Function Definition
  rev = 0while(Number > 0):
    rem = Number %10
    rev = (rev *10) + rem
    Number = Number //10return rev

Number = int(input())
rev = Reverse(Number)  # Function Call
print("%d" %rev)
   


P1.B # writa program to perform the matrix additional, 
Multiplication and Transpose operation.


Code:matrix additional

#Python program to perform matrix addition
mat1 = [[1, 2], [3, 4]] #the first matrix
mat2 = [[1, 2], [3, 4]] #the second matrix
mat3 = [[0, 0], [0, 0]] #an empty matrix to store the result

#adding two matrices
for i in range(0, 2):
  for j in range(0, 2):
    mat3[i][j] = mat1[i][j] + mat2[i][j]

#printing the resultant matrix
print("Addition of two matrices")
for i in range(0, 2):
  for j in range(0, 2):
    print(mat3[i][j], end = " ")
  print()


Code:Multiplication

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)


Code:Transpose

#Original Matrix
x = [[1,2],[3,4],[5,6]]
result = [[0, 0, 0], [0, 0, 0]]
# Iterate through rows
for i in range(len(x)):
   #Iterate through columns
   for j in range(len(x[0])):
      result[j][i] = x[i][j]
   for r in Result
print(r)




      

