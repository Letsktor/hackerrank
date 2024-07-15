import re
n=int(input())
for i in range(n):
    s=input()
    m=re.match(r'^[7-9][0-9]{9}',s)
    try:
        if len(s)==10:
            if  m.group(0):
                
                print("YES")
        else:
            print("NO")
    except:
        print("NO")
