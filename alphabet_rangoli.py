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