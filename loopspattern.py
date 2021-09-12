n = int(input())
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end="")
    m=j
    for l in range(1,2*i-1,1):
        print(m,end="")
    p=1
    f=i+1
    while p<=(n-i):
        print(f,end="")
        p=p+1
        f=f+1
    print()
for i in range(1,n,1):
    r=n
    for j in range(1,n-i+1,1):
        print(r,end="")
        r=r-1
    k=i+1
    for t in range(1,2*i+1,1):
        print(k,end="")
    p=1
    f=i+2
    while p<=(n-i-1):
        print(f,end="")
        p=p+1
        f=f+1
    print()