n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
q=6
o=4
for i in range(o):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(i,o):
        print(q,end=" ")
    for j in range(i,o-1):
        print(q,end=" ")
    q+=1
    print()