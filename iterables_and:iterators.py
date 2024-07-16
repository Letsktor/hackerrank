import itertools
n=int(input())
li=input().split()
k=int(input())
temp=[]
size=0
for e in itertools.permutations(li,k):
    size+=1
    if 'a' in e:
        temp.append(e)
print(len(temp)/size)
