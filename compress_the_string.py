import itertools
s=input()
for g,k in itertools.groupby(s,key=None):
    print((len(list(k)),int(g)),end=" ")
