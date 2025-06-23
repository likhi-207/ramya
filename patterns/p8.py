n = int(input())
for i in range(n):
    if i<=n//2:
        for i in range(i+1):
            print("*",end=" ")
    if i>n//2:
        for i in range(n-i):
            print("*",end=" ")  
    print()               

        