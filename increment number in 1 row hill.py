n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
        p=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1

    p=3
    for j in range(i):
       #p=3
       print(p,end=" ")
    p+=1
    print()
        