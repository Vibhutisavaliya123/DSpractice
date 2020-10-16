#P1.B # writa program to perform the matrix additional, 
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
result = [[0, 0], [0,0],[0,0]]
# Iterate through rows
for i in range(len(x)):
   #Iterate through columns
   for j in range(len(x[0])):
      result[j][i] = x[i][j]
   for r in Result
print(r)

