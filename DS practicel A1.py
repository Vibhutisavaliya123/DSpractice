#Write a program to store the elements in
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

      

