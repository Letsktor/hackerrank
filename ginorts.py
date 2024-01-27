"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""
s=input()
odddi=[]
evendi=[]
lower=[]
upper=[]
for e in s:
    if e.isdigit():
        if int(e)%2==0:
            evendi.append(e)
        else:
            odddi.append(e)
    else:
        if e.isupper():
            upper.append(e)
        else:
            lower.append(e)
odddi.sort()
evendi.sort()
lower.sort()
upper.sort()
for e in lower:
    print(e, end="")
for e in upper:
    print(e,end="")
for e in odddi:
    print(e,end="")
for e in evendi:
    print(e,end="")