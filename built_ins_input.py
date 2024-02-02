"""
input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
Task

You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Constraints
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True
Explanation


Hence, the output is True.
"""
s=input().split()
x=int(s[0])
k=int(s[1])
pol=input()
li=[]
for e in pol:
    if e=="x":
        li.append(str(x));
    else:
        li.append(e)
if eval("".join(li))==k:
    print(True)
else:
    print(False)

