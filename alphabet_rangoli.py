"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    j=(int(n)*2)-2
    for i in range((((int(n)*2)//2))):
            print("-"*j,end="")
            for g in range(n,n-i-1,-1):
                if n-i-1==n-1:
                    print(chr(96+int(g)),end="")
                else:
                     print(chr(96+int(g)),end="")
                     print("-",end="")
            if  not i==0:
                for g in range(n-i,n):
                    if n-i==n-1:
                        print(chr(97+int(g)),end="")
                    else:
                        print(chr(97+int(g)),end="")
                        if not g==n-1:
                            print("-",end="")
            print("-"*j,end="")
            print()
            j=j-2
    j=2
    for i in range((((int(n)*2)//2))-2,-1,-1):
            print("-"*j,end="")
            for g in range(n,n-i-1,-1):
                    if n-i-1==n-1:
                        print(chr(96+int(g)),end="")
                    else:
                        print(chr(96+int(g)),end="")
                        print("-",end="")
            if  not i==0:
                for g in range(n-i,n):
                        if n-i==n-1:
                            print(chr(97+int(g)),end="")
                        else:
                            print(chr(97+int(g)),end="")
                            if not g==n-1:
                                print("-",end="")
            print("-"*j,end="")
            print()
            j=j+2


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
