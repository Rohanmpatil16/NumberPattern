n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()
m=4   
q=4
for i in range(m):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(i,m):
        print(q,end=" ")
    for i in range(i,m-1):
        print(q,end=" ")
    q-=1
    print()