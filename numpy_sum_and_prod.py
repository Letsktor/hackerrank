"""
sum

The sum tool returns the sum of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod

The prod tool returns the product of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

Task

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
Explanation

The sum along axis  = [ ]
The product of this sum = 
"""

import numpy

s=input()
n=int(s.split()[0])
m=int(s.split()[1])
li=[]
for i in range(m):
    temp=input().split()
    for j in range(len(temp)):
        temp[j]=int(temp[j])
    li.append(temp)
my_array=numpy.array(li)
print(numpy.prod(numpy.sum(my_array,axis=0),axis=None))