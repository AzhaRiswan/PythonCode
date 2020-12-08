#Python Array
#We need to import a library called array or the following way
from array import *

# Define the array with type i defined the signed integer
A = array( 'i' , [5,9,8,12,3])

# To print the values of the array
print(A)

#To print the each value of the array
for i in range(len(A)):
    print(A[i])


# OR
for e in A:
    print(e)

#Functions used with array
#To get to know about memory address and size of the array
    print(A.buffer_innfo())


#To know about the type of the array
    print(A.typecode)

#To reverse the values of an array
    A.reverse()

#If we don't know the type of an existing array and want extract the values for a new array
    NewArr = array(A.typecode, (a for a in A))
    print(NewArr)
