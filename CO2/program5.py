n=int(input("enter the no of rows"))
for i in range(1,n+1):
    m=i
    for j in range(1,i+1):
        print(m,end=' ')
        m=m+i
    print()